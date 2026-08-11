import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"


gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=API_KEY)

system_prompt = """You are a senior machine learning engineer. Your company is hiring Junior ML Engineers i.e., 
Freshers with zero experience. Give me 5 questions you would ask the candidate"""

user_prompt_prefix = "Good morning sir."

message = "Hello, gemini! This is my first message to you! Hi!"

messages = [{"role":"system", "content":system_prompt}, {"role":"user", "content":user_prompt_prefix}]


response = gemini.chat.completions.create(model="gemini-3.1-flash-lite", messages=messages)
print(response.choices[0].message.content)