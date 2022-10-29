from typing import Generator
from app.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_db_now() -> Generator:
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()
