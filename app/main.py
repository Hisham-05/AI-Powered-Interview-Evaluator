from fastapi import FastAPI
from app.api import candidate
from app.database import Base, engine
from app.models.candidate import Candidate
app = FastAPI()

app.include_router(candidate.router)

Base.metadata.create_all(engine)

@app.get("/")
def home():
    return {"message": "Welcome to AI Interview Evaluator"}