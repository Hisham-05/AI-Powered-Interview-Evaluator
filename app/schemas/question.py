from pydantic import BaseModel

class CreateQuestion(BaseModel):
    interview_id: int
    question : str

class QuestionResponse(BaseModel):
    id : int
    interview_id : int
    question : str

class UpdateQuestion(BaseModel):
    interview_id: int
    question : str