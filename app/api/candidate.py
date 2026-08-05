from fastapi import APIRouter
from app.schemas.candidate import CandidateResponse, CreateCandidate
from app.models.candidate import Candidate
from app.database import sessionLocal

router = APIRouter()
@router.post("/candidates", response_model=CandidateResponse)
def create_candidate(candidate: CreateCandidate):
    db_candidate = Candidate(name=candidate.name, email=candidate.email, password=candidate.password)
    session = sessionLocal()
    session.add(db_candidate)
    session.commit()
    session.refresh(db_candidate)
    session.close()
    return db_candidate