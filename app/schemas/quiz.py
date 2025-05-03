from pydantic import BaseModel

class QuestionCreate(BaseModel):
    question_text: str
    correct_answer: str

class QuestionOut(QuestionCreate):
    id: int
    class Config:
        orm_mode = True
