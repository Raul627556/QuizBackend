from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Cambia esto según tu config real
DATABASE_URL = "postgresql://postgres:password@db:5432/quizdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def init_db():
    from app.models import question, answer  # importa los modelos para que Base los registre
    Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()