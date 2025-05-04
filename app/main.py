from fastapi import FastAPI
from app.database import init_db
from app.api import api_router

app = FastAPI(title="Quiz App")

@app.on_event("startup")
def startup():
    init_db()

app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Quiz API funcionando"}
