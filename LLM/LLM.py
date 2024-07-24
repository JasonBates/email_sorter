

from config.config import OPENAI_API_KEY
from openai import OpenAI
class LLMService:
    def __init__(self, API_key):
        self.client = OpenAI(api_key=API_key)
    
    def get_response(self, prompt):
        response = self.client.chat.completions.create(model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ])
        return response.choices[0].message.content.strip()
    
    def get_json_response_with_context(self, prompt, context):
        response = self.client.chat.completions.create(model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who always responds in json format"},
                {"role": "user", "content": prompt},
                {"role": "system", "content": context},
                ], 
            response_format={"type": "json_object"})
        return response.choices[0].message.content.strip()
