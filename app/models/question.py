from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    
    question = Column(String)

    interview_id = Column(Integer, ForeignKey("interviews.id"))

    interview_att = relationship("Interview", back_populates="question_att")

