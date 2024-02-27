# LLM_Chat_Templater
 
 Different model has different way of templating their prompts before sending to the model. FastChat has a templater that wraps around many models, but the templater isn't intuitive to use. IN MY OPINION, OpenAI's format (system, user, assistant, ... user) seem to be the easiest to comply. 

This repo is adapted from [fastchat](https://github.com/lm-sys/FastChat/blob/main/fastchat/conversation.py), and an OpenAI templating format is wrapped around the fastchat's templater. Best part, no additional libraries required ontop of Python's native libraries.

Supported models: 
```
['airoboros_v1', 'airoboros_v2', 'airoboros_v3', 'alpaca', 'aquila', 'aquila-chat', 'aquila-legacy', 'aquila-v1', 
'baichuan-chat', 'baichuan2-chat', 'baize', 'billa', 
'catppt', 'chatglm', 'chatglm2', 'chatglm3', 'chatgpt', 'chinese-alpaca2', 'claude', 'codegeex', 'cutegpt', 
'deepseek-chat', 'deepseek-coder', 'dolly_v2', 'dolphin-2.2.1-mistral-7b', 
'falcon', 'falcon-chat', 
'h2ogpt', 
'internlm-chat', 
'koala_v1', 
'lemur-70b-chat', 'llama-2', 'llama2-chinese', 'llava-chatml', 
'manticore', 'metamath', 'metharme', 'mistral', 'mistral-7b-openorca', 'mpt-30b-chat', 'mpt-30b-instruct', 'mpt-7b-chat', 
'Nous-Hermes-2-Mixtral-8x7B-DPO', 
'oasst_llama', 'oasst_pythia', 'open-orca', 'openbuddy', 'openchat_3.5', 'OpenHermes-2.5-Mistral-7B', 'orca-2', 
'phind', 'phoenix', 'polyglot_changgpt', 
'qwen-7b-chat', 
'ReaLM-7b-v1', 'redpajama-incite', 'Robin', 'rwkv', 
'snoozy', 'solar', 'stable-vicuna', 'stablelm', 'starchat', 
'tenyxchat', 'tigerbot', 'TinyLlama', 'tulu', 
'vicuna_v1.1', 'vigogne_chat_v2', 'vigogne_chat_v3', 'vigogne_instruct', 
'xdan-v1', 'xgen', 
'Yi-34b-chat', 'yuan', 'yuan2', 
'zephyr']
```

Example usage:
```
from prompt_template import OpenAITemplate

templater = OpenAITemplate('llama-2')
conversation = [
    {
        "role":"system",
        "content": "You're a helpful, respectful and honest assistant"
    },
    {
        "role":"user",
        "content": "Hello!" 
    },
    {
        "role":"assistant",
        "content": "Hi!" 
    },
    {
        "role":"user",
        "content": "How are you?" 
    }
]
print(templater(conversation))

# [INST] <<SYS>>
# You're a helpful, respectful and honest assistant
# <</SYS>>
#
# Hello! [/INST] Hi! </s><s>[INST] How are you? [/INST]

```