import os

file_path = os.path.join(os.path.dirname(__file__), 'LLM', 'prompt.md')

with open('LLM/prompt.md', 'r') as file:
    # Read the content of the file into a string
    content = file.read()
    
print(content)