from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import quiz as schemas
from app.crud import quiz as crud
from app.database import SessionLocal


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/questions", response_model=schemas.QuestionOut)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db, question)

@router.get("/questions", response_model=list[schemas.QuestionOut])
def read_questions(db: Session = Depends(get_db)):
    return crud.get_questions(db)
