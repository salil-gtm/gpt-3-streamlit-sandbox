import json
import openai
from fastapi import FastAPI
from pydantic import BaseModel
from gpt import GPT
from gpt import Example

server_url = "http://127.0.0.1:8000"

with open('config.json') as f:
    data = json.load(f)
openai.api_key = data['API_KEY']

app = FastAPI(title="GPT3 Streamlit Sandbox",
    description="API Docs",
    version="1.0.0",)

gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

class Training(BaseModel):
    input: str
    output: str

@app.post("/add_example")
def example_endpoint(item:Training):
    gpt.add_example(Example(item.input, item.output))
    return "Example Added !"

@app.post("/ask_gpt")
def user_endpoint(prompt):
    output = gpt.submit_request(prompt)
    result = output.choices[0].text
    return result
