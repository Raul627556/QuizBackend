from fastapi import APIRouter
from . import question, category

api_router = APIRouter()
api_router.include_router(question.router)
api_router.include_router(category.router)