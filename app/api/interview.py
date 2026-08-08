from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from app.database import sessionLocal
from app.models.interview import Interview
from app.models.candidate import Candidate
from app.schemas.interview import CreateInterview, InterviewResponse

router = APIRouter()

@router.post("/interviews", response_model = InterviewResponse)
def create_interview(interview: CreateInterview):
    session = sessionLocal()
    try:
        statement = select(Candidate).where(Candidate.id == interview.candidate_id)
        result = session.execute(statement)
        candidate = result.scalar_one_or_none()

        if candidate is None:
            raise HTTPException(status_code = 404, detail = "Candidate not found")

        db_interview = Interview(candidate_id = interview.candidate_id, company = interview.company, role = interview.role)
        session.add(db_interview)
        session.commit()
        session.refresh(db_interview)

        return db_interview

    finally:
        session.close()