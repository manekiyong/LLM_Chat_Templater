import torch
from transformers import AutoTokenizer, LlamaForCausalLM

from prompt_template import OpenAITemplate


if __name__ == "__main__":
    model_name = "meta-llama/Llama-2-7b-chat-hf" 
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = LlamaForCausalLM.from_pretrained(model_name, device_map="auto", torch_dtype=torch.float16)
    tokenizer = AutoTokenizer.from_pretrained(model_name)


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
    prompt = templater(conversation) # Returns str

    prompt_tensor = tokenizer(prompt, return_tensors='pt').to(device)
    input_len = len(prompt_tensor.input_ids[0])
    response_tensor = model.generate(prompt_tensor.input_ids, max_new_tokens=512)
    response = tokenizer.decode(response_tensor[0][input_len:], skip_special_tokens=True)
    print(response)
