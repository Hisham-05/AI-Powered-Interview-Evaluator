from fastapi import APIRouter
from app.schemas.candidate import CreateCandidate, CandidateResponse

router = APIRouter()

@router.post("/candidates", response_model=CandidateResponse)
def create_candidate(candidate: CreateCandidate):
    return candidate