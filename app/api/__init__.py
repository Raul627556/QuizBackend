from fastapi import APIRouter
from . import question

api_router = APIRouter()
api_router.include_router(question.router)
