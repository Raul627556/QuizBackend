from typing import List, Optional
from pydantic import BaseModel

class AnswerBase(BaseModel):
    text: str
    is_correct: bool

class AnswerCreate(AnswerBase):
    pass

class AnswerRead(AnswerBase):
    id: int

    class Config:
        orm_mode = True

class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    answers: List[AnswerCreate]  # Al crear una pregunta, se envían las 4 respuestas

class QuestionRead(QuestionBase):
    id: int
    answers: List[AnswerRead]  # Al leer una pregunta, se devuelven sus respuestas

    class Config:
        orm_mode = True
