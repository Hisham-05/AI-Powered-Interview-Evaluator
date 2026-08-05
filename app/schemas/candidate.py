from pydantic import BaseModel

class CreateCandidate(BaseModel):
    name: str
    email: str
    password: str

class CandidateResponse(BaseModel):
    name: str
    email: str