from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.question import QuestionCreate, QuestionRead
from app.models.question import Question
from app.models.answer import Answer
from app.models.user import User
from app.database import SessionLocal
from app.api.deps import get_current_user
from typing import List

router = APIRouter(prefix="/questions", tags=["Questions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=QuestionRead)
def create_question(
    question: QuestionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if len(question.answers) != 4:
        raise HTTPException(status_code=400, detail="Debe haber exactamente 4 respuestas.")

    if sum(a.is_correct for a in question.answers) != 1:
        raise HTTPException(status_code=400, detail="Debe haber UNA única respuesta correcta.")

    db_question = Question(
        text=question.text,
        category_id=question.category_id
    )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    for answer in question.answers:
        db.add(Answer(
            text=answer.text,
            is_correct=answer.is_correct,
            question_id=db_question.id
        ))
    db.commit()
    db.refresh(db_question)
    return db_question

@router.get("/", response_model=list[QuestionRead])
def get_questions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Question).all()

@router.get("/{question_id}", response_model=QuestionRead)
def get_question(
    question_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    return question

@router.get("/by-category/{category_id}", response_model=List[QuestionRead])
def get_questions_by_category(
    category_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    questions = db.query(Question).filter(Question.category_id == category_id).all()
    if not questions:
        raise HTTPException(status_code=404, detail="No se encontraron preguntas para esta categoría.")
    return questions