from llm import llmApiCall
from speechToText import recordMic
messageContents = [
    {"role": "system", "content": "You are a professional assistant"},
    {"role": "user", "content": "Hello"}
    ]
# print(recordMic())

for token in llmApiCall(messageContents):
    print(token, end='', flush=True)
#print(llmApiCall(messageContents))
