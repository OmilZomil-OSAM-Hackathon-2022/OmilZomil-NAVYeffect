from app.db.init_db import init_db
from app.db.session import SessionLocal


db = SessionLocal()
init_db(db)
