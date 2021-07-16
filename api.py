import json
import openai
import pandas as pd
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

# Example Training
print("Bulk Example Training")
example_data = pd.read_csv("examples.csv")
for count, row in example_data.iterrows():
    print("Input : ", row['Input'],"Ouput : ", row['Ouput'])
    gpt.add_example(Example(row['Input'], row['Ouput']))
print("All Examples Added !")

class Training(BaseModel):
    input: str
    output: str

class Testing(BaseModel):
    prompt: str

@app.post("/add_example")
def example_endpoint(item:Training):
    gpt.add_example(Example(item.input, item.output))
    return "Example Added !"

@app.post("/ask_gpt")
def user_endpoint(item:Testing):
    result = gpt.get_top_reply(item.prompt)
    return result
