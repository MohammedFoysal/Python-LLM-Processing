from typing import List

def invoke_llm(user_input: str, model_name: str, chunks: List[str]):
    print("LLM received request:", { "input": user_input, "model": model_name, "num_of_chunks": len(chunks) })

def main(user_input: str, model_name: str):
    pass

if __name__ == "__main__":
    main("Does Acme Org support remote working", "gpt-4o")
