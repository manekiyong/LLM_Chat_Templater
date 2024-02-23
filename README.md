# LLM_Chat_Templater
 
 Different model has different way of templating their prompts before sending to the model. FastChat has a templater that wraps around many models, but the templater isn't intuitive to use. IN MY OPINION, OpenAI's format (system, user, assistant, ... user) seem to be the easiest to comply. 

This repo is adapted from [fastchat](https://github.com/lm-sys/FastChat/blob/main/fastchat/conversation.py), and an OpenAI templating format is wrapped around the fastchat's templater. Best part, no additional libraries required ontop of Python's native libraries.

Supported models: 
```
['vicuna_v1.1', 'airoboros_v1', 'airoboros_v2', 'airoboros_v3', 'koala_v1', 'alpaca', 'chatglm', 'chatglm2', 'chatglm3', 'codegeex', 'dolly_v2', 'oasst_pythia', 'oasst_llama', 'openchat_3.5', 'tenyxchat', 'deepseek-coder', 'tulu', 'stablelm', 'baize', 'rwkv', 'openbuddy', 'phoenix', 'ReaLM-7b-v1', 'chatgpt', 'claude', 'metamath', 'mpt-7b-chat', 'mpt-30b-chat', 'lemur-70b-chat', 'mpt-30b-instruct', 'billa', 'redpajama-incite', 'h2ogpt', 'Robin', 'snoozy', 'manticore', 'falcon', 'polyglot_changgpt', 'tigerbot', 'xgen', 'internlm-chat', 'starchat', 'baichuan-chat', 'baichuan2-chat', 'mistral', 'llama-2', 'chinese-alpaca2', 'cutegpt', 'open-orca', 'mistral-7b-openorca', 'dolphin-2.2.1-mistral-7b', 'OpenHermes-2.5-Mistral-7B', 'Nous-Hermes-2-Mixtral-8x7B-DPO', 'qwen-7b-chat', 'Yi-34b-chat', 'aquila-chat', 'aquila-legacy', 'aquila', 'aquila-v1', 'llama2-chinese', 'vigogne_instruct', 'vigogne_chat_v2', 'stable-vicuna', 'vigogne_chat_v3', 'falcon-chat', 'phind', 'metharme', 'xdan-v1', 'zephyr', 'catppt', 'TinyLlama', 'orca-2', 'deepseek-chat', 'yuan2', 'solar', 'yuan', 'llava-chatml']
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
```