from app.database import sessionLocal
from app.models.evaluation import Evaluation
from app.models.response import Response
from app.schemas.evaluation import CreateEvaluation, EvaluationResponse
from sqlalchemy import select
from fastapi import HTTPException, APIRouter

router = APIRouter()

@router.post("/evaluations", response_model=EvaluationResponse)
def create_evaluation(evaluation: CreateEvaluation):
    session = sessionLocal()
    try:
        statement = select(Response).where(Response.id == evaluation.response_id)
        result = session.execute(statement)
        response = result.scalar_one_or_none()

        if response is None:
            raise HTTPException(status_code=404, detail="Response not found")

        evaluation_db = Evaluation(response_id=evaluation.response_id,
                                         accuracy_score=evaluation.accuracy_score,
                                         relevance_score=evaluation.relevance_score,
                                         technical_score=evaluation.technical_score,
                                         grammar_score=evaluation.grammar_score,
                                         confidence_score=evaluation.confidence_score,
                                         filler_word_count=evaluation.filler_word_count,
                                         feedback=evaluation.feedback,
                                         strengths=evaluation.strengths)
        session.add(evaluation_db)
        session.commit()
        session.refresh(evaluation_db)
        return evaluation_db

    finally:
        session.close()

@router.get("/evaluations", response_model=list[EvaluationResponse])
def get_evaluations():
    session = sessionLocal()
    statement = select(Evaluation)
    result = session.execute(statement)
    evaluations = result.scalars().all()
    session.close()
    return evaluations

@router.get("/evaluations/{id}", response_model=EvaluationResponse)
def get_single_evaluation(id: int):
    session = sessionLocal()
    try:
        statement = select(Evaluation).where(Evaluation.id == id)
        result = session.execute(statement)
        evaluation = result.scalar_one_or_none()

        if evaluation is None:
            raise HTTPException(status_code=404, detail="Evaluation not found")

        return evaluation

    finally:
        session.close()

@router.delete("/evaluations/{id}")
def delete_evaluation(id:int):
    session = sessionLocal()
    try:
        statement = select(Evaluation).where(Evaluation.id == id)
        result = session.execute(statement)
        evaluation = result.scalar_one_or_none()

        if evaluation is None:
            raise HTTPException(status_code=404, detail="Evaluation not found")

        session.delete(evaluation)
        session.commit()
        return "Evaluation deleted successfully"

    finally:
        session.close()