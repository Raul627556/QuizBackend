from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.question import QuestionCreate, QuestionRead
from app.models.question import Question
from app.models.answer import Answer
from app.database import SessionLocal

router = APIRouter(prefix="/questions", tags=["Questions"])

# Dependency para obtener la DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=QuestionRead)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    if len(question.answers) != 4:
        raise HTTPException(status_code=400, detail="Debe haber exactamente 4 respuestas.")

    if sum(a.is_correct for a in question.answers) != 1:
        raise HTTPException(status_code=400, detail="Debe haber UNA única respuesta correcta.")

    db_question = Question(text=question.text)
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
def get_questions(db: Session = Depends(get_db)):
    return db.query(Question).all()

@router.get("/{question_id}", response_model=QuestionRead)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = db.query(Question).filter(Question.id == question_id).first()
    if not question:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    return question
