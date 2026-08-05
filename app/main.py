from fastapi import FastAPI
from app.api import candidate

app = FastAPI()

app.include_router(candidate.router)

@app.get("/")
def home():
    return {"message": "Welcome to AI Interview Evaluator"}

