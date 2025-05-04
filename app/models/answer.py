from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from ..database import Base

class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False, nullable=False)

    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False)
    question = relationship("Question", back_populates="answers")