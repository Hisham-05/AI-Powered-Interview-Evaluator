from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = "postgresql://postgres:REDACTED@localhost:5435/ai_interview_evaluator_project"

engine =create_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass

sessionLocal = sessionmaker(bind=engine)