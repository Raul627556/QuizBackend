from sqlalchemy.orm import Session
from app.models import quiz as models
from app.schemas import quiz as schemas


def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question

def get_questions(db: Session):
    return db.query(models.Question).all()
