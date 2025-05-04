from typing import List, Optional
from pydantic import BaseModel
from .answer import AnswerCreate, AnswerRead


class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    category_id: int
    answers: List[AnswerCreate]

class QuestionRead(QuestionBase):
    id: int
    answers: List[AnswerRead]

    class Config:
        orm_mode = True
