# Creating the GPT-2 model from scratch (Radford et al., 2019)
# Model Specifications:
# - Number of parameters: 124
# - Number of layers: 12
# - Number of dimensions: 768

# Major changes from the transformer architecture:
# - The model is decoder only(no encoder stack + no cross attention)
# - The LayerNorm is applied before each block instead of after
# - The final Linear Classifier is preceded by a LayerNorm
# - The model is trained with a language modeling objective

# Imports
from dataclasses import dataclass
from networkx import config
import torch
import torch.nn as nn
import torch.nn.functional as F



class CausalSelfAttention(nn.Module):

    def __init__(self,config):
        super().__init__()
        assert config.n_embd % config.n_head == 0 # ensure that the model dimensions are divisible by the number of heads
        self.c_attn=nn.Linear(config.n_embd, 3*config.n_embd) # linear layer to compute query, key and value vectors
        self.c_proj=nn.Linear(config.n_embd, config.n_embd) # linear layer to project the output of the attention mechanism back to the model dimensions
        self.attn_dropout=nn.Dropout(0.1) # dropout for attention weights
        self.resid_dropout=nn.Dropout(0.1) # dropout for output of attention mechanism
        self.n_head=config.n_head # number of attention heads
        self.n_embd=config.n_embd # model dimensions

    def forward(self,x):
        B,T,C=x.size() # batch size, sequence length and model dimensions
        # calculate query, key and value vectors for all heads in batch and move head forward to be the batch dimension
        # nh = number of heads, hs = head size (n_embd // n_head), C = n_embd = nh * hs
        # in GPT-2, nh = 12, hs = 64, so C= nh * hs = 768
        qkv=self.c_attn(x) # compute query, key and value vectors
        q,k,v= qkv.split(self.n_embd, dim=2) # split the output of the linear layer into query, key and value tensors
        q=q.view(B,T,self.n_head,C//self.n_head).transpose(1,2) # reshape and permute to separate heads
        k=k.view(B,T,self.n_head,C//self.n_head).transpose(1,2) # reshape and permute to separate heads
        v=v.view(B,T,self.n_head,C//self.n_head).transpose(1,2) # reshape and permute to separate heads
        
        # attention materializes the large (T,T) attention matrix for queries and keys
        att = (q @ k.transpose(-2,-1)) * (1.0 / torch.sqrt(k.size(-1))) # compute attention scores
        att = att.masked_fill(self.bias[:,:,:T,:T] == 0, float('-inf')) # apply causal mask to ensure that attention is only applied to previous tokens in the sequence
        att = F.softmax(att, dim=-1) # apply softmax to get attention

        y = att @ v # compute weighted sum of value vectors
        y = y.transpose(1,2).contiguous().view(B,T,C) # reshape back to original dimensions with concatentation of heads
        y = self.resid_dropout(self.c_proj(y)) # project back to model dimensions and apply dropout
        return y

class MLP(nn.Module):

    def __init__(self,config):
        super().__init__()
        self.c_fc=nn.Linear(config.n_embd, 4*config.n_embd) # first linear layer where 4 is the expansion factor
        self.gelu= nn.GELU(approximate='tanh') # activation function with approximation from GELU paper (Hendrycks and Gimpel, 2016)
        self.c_proj=nn.Linear(4*config.n_embd, config.n_embd) # second linear layer

class Block(nn.Module):

    def __init__(self,config):
        super().__init__()
        self.ln_1=nn.LayerNorm(config.n_embd) # layer norm 1
        self.attn=CausalSelfAttention(config) # self attention layer acting as reducer for the input to the feed forward layer
        self.ln_2=nn.LayerNorm(config.n_embd) # layer norm 2
        self.mlp=MLP(config) # feed forward layer acting as mapper for the input to the next block

    def forward(self,x):
        x=x+self.attn(self.ln_1(x)) # self attention with residual connection
        x=x+self.mlp(self.ln_2(x)) # feed forward with residual connection
        return x
    
@dataclass
class GPT2Config:
    block_size: int = 1024 # max seq length of inputs to the model
    vocab_size:int=50257 # number of unique tokens in the dataset (65 for char level, 50257 for word level)
    n_layer:int=12 # number of transformer blocks
    n_head:int=12 # number of attention heads in each block
    n_embd:int=768 # model dimensions

class GPT2(nn.Module): 

    def __init__(self,config):
        super().__init__()
        self.config=config
        self.transformer=nn.ModuleDict(dict(
            wte= nn.Embedding(config.vocab_size, config.n_embd), # token embedding table
            wpe= nn.Embedding(config.block_size, config.n_embd), # position embedding table
            h= nn.ModuleList([Block(config) for _ in range(config.n_layer)]), # transformer blocks
            ln_f= nn.LayerNorm(config.n_embd), # final layer norm
        ))
        self.lm_head=nn.Linear(config.n_embd, config.vocab_size, bias=False) # language modeling head



    @classmethod
    def from_pretrained(cls, model_type):
        """Loads pretrained GPT-2 model weights from huggingface"""
        assert model_type in {'gpt2', 'gpt2-medium', 'gpt2-large', 'gpt2-xl'}
        from transformers import GPT2LMHeadModel
        print("loading weights from pretrained gpt: %s" % model_type)

        # n_layer, n_head and n_embd are determined from model_type
        config_args = {
            'gpt2':         dict(n_layer=12, n_head=12, n_embd=768),  # 124M params
            'gpt2-medium':  dict(n_layer=24, n_head=16, n_embd=1024), # 350M params
            'gpt2-large':   dict(n_layer=36, n_head=20, n_embd=1280), # 774M params
            'gpt2-xl':      dict(n_layer=48, n_head=25, n_embd=1600), # 1558M params
        }[model_type]
        config_args['vocab_size'] = 50257 # always 50257 for GPT model checkpoints
        config_args['block_size'] = 1024 # always 1024 for GPT model checkpoints
        # create a from-scratch initialized minGPT model
        config = GPT2Config(**config_args)
        model = GPT2(config)
        sd = model.state_dict()
        sd_keys = sd.keys()
        sd_keys = [k for k in sd_keys if not k.endswith('.attn.bias')] # discard this mask / buffer, not a param

        # init a huggingface/transformers model
        model_hf = GPT2LMHeadModel.from_pretrained(model_type)
        sd_hf = model_hf.state_dict()

        # copy while ensuring all of the parameters are aligned and match in names and shapes
        sd_keys_hf = sd_hf.keys()
        sd_keys_hf = [k for k in sd_keys_hf if not k.endswith('.attn.masked_bias')] # ignore these, just a buffer
        sd_keys_hf = [k for k in sd_keys_hf if not k.endswith('.attn.bias')] # same, just the mask (buffer)
        transposed = ['attn.c_attn.weight', 'attn.c_proj.weight', 'mlp.c_fc.weight', 'mlp.c_proj.weight']
        # basically the openai checkpoints use a "Conv1D" module, but we only want to use a vanilla Linear
        # this means that we have to transpose these weights when we import them
        assert len(sd_keys_hf) == len(sd_keys), f"mismatched keys: {len(sd_keys_hf)} != {len(sd_keys)}"
        for k in sd_keys_hf:
            if any(k.endswith(w) for w in transposed):
                # special treatment for the Conv1D weights we need to transpose
                assert sd_hf[k].shape[::-1] == sd[k].shape
                with torch.no_grad():
                    sd[k].copy_(sd_hf[k].t())
            else:
                # vanilla copy over the other parameters
                assert sd_hf[k].shape == sd[k].shape
                with torch.no_grad():
                    sd[k].copy_(sd_hf[k])

        return model
    

    # -----------------------------------------------------------------------------

model= GPT2.from_pretrained('gpt2') # load the pretrained weights from HuggingFace's GPT-2 checkpoint
print("Model loaded successfully with pretrained weights from HuggingFace's GPT-2 checkpoint!")