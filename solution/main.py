from typing import List
from data import data

models = {
    "gpt-3.5-turbo": 50,
    "gpt-4": 100,
    "gpt-4o": 200,
}

def split_text(text: str, max_tokens_per_chunk: int) -> List[str]:
    tokens = text.split()
    chunks = []

    for i in range(0, len(tokens), max_tokens_per_chunk):
        chunk = ' '.join(tokens[i:i + max_tokens_per_chunk])
        chunks.append(chunk)

    return chunks

def invoke_llm(user_input: str, model_name: str, chunks: List[str]):
    print("LLM received request:", { "input": user_input, "model": model_name, "num_of_chunks": len(chunks) })

def main(user_input: str, model_name: str):
    chunks = split_text(data, models[model_name])

    invoke_llm(user_input, model_name, chunks)

if __name__ == "__main__":
    main("What is the capital of france?", "gpt-4o")
