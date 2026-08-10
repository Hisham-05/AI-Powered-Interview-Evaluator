from fastapi import FastAPI
from app.api import candidate
from app.api import interview
from app.api import question
from app.database import Base, engine
from app.models.candidate import Candidate
from app.models.interview import Interview
from app.models.question import Question
app = FastAPI()

app.include_router(candidate.router)
app.include_router(interview.router)
app.include_router(question.router)
Base.metadata.create_all(engine)

@app.get("/")
def home():
    return {"message": "Welcome to AI Interview Evaluator"}