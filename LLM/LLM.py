

from config.config import OPENAI_API_KEY
from openai import OpenAI

# client = OpenAI(api_key=OPENAI_API_KEY)

# # Example of making a request to OpenAI's API using the Chat Completions endpoint
# response = client.chat.completions.create(model="gpt-3.5-turbo",
# messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Tell me a joke."}
# ])

# # print(response.choices[0].message.content.strip())


class LLMService:
    def __init__(self, API_key):
        self.client = OpenAI(api_key=API_key)
    
    def get_response(self, prompt):
        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ])
        return response.choices[0].message.content.strip()
    
    def get_response_with_context(self, prompt, context):
        response = self.client.chat.completions.create(model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
                {"role": "system", "content": context}
            ])
        return response.choices[0].message.content.strip()



LLM = LLMService(OPENAI_API_KEY)
# result = LLM.get_response("Tell me I'm beautiful.")
# print(result)

result2 = LLM.get_response_with_context("what should I do as a career?", "I have a degree in engineering and a love of boats and the sea.")
print(result2)
