from sqlalchemy.orm import relationship

from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Interview(Base):
    __tablename__ = "interviews"

    id = Column(Integer, primary_key=True)

    candidate_id = Column(Integer, ForeignKey("candidates.id"))

    company = Column(String)

    role = Column(String)

    candidates = relationship("Candidate", back_populates = "interviews")


