from fastapi import FastAPI
from app.api import quiz

app = FastAPI()
app.include_router(quiz.router, prefix="/api")
