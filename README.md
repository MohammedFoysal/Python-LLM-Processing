# Python Interview Test - LLM Data Processing

## Task

Context data is often packaged along with the user's input when calling Large Language Models (LLMs). But this LLM can only manage a certain number of tokens per chunk.

- Your task is to call the simulated LLM `invoke_llm` function using the user's input, model selection and the context data from `data.py`.
- You will need to break the context data into chunks based on the number of tokens (for this exercise you can think of a token as a single word in the string).

The following models and their max tokens per chunk are listed below:

```
- gpt-3.5-turbo allows 50 tokens per chunk
- gpt-4 allows 100 tokens per chunk
- gpt-4o allows 200 tokens per chunk
```

Remember to write tests and build the best solution possible to showcase your skills.

## Notes

- You do not need to implement any network calls or actual LLM interactions.
- You can only use the standard python libraries
- You should not modify the `invoke_llm` function

## Extensions
1. After every LLM request we need to charge the user based on their usage. Log out how much the user is required to pay in pounds based on the following rules:

```
- gpt-3.5-turbo charges 3p per token
- gpt-4 charges 20p per token
- gpt-4o charges 10p per token
```

2. Write a function that analyses the context data to count how often each word appears. Print the 10 most frequent words in order from most to least common.

3. To save on token costs, clean the context data passed into the LLM by removing common words e.g. "the", "and", "a", "to"
