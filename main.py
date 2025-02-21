from llm import llmApiCall
from speechToText import recordMic
messageContents = [
    {"role": "system", "content": "You are a professional assistant"},
    {"role": "user", "content": "Hello"}
    ]
print(recordMic())
print(llmApiCall(messageContents))
