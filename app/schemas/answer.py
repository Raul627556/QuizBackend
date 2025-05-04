from pydantic import BaseModel

class AnswerBase(BaseModel):
    text: str
    is_correct: bool

class AnswerCreate(AnswerBase):
    pass

class AnswerRead(AnswerBase):
    id: int
    question_id: int

    class Config:
        orm_mode = True
