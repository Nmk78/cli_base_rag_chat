from langchain_ollama import OllamaLLM
from src.config_loader import load_config

config = load_config()

def get_llm(
    model=config['llm']['model'],
    temperature=config['llm']['temperature'],
    max_tokens=config['llm']['max_tokens'],
    streaming=True
):
    return OllamaLLM(
        model=model,
        temperature=temperature,
        max_tokens=max_tokens,
        streaming=streaming
    )
