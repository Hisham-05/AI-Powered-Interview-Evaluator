from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    email = Column(String)

    password = Column(String)

    interviews = relationship("Interview", back_populates = "candidates")