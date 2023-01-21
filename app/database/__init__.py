
"""Database module"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.config import DB_URL

engine = create_engine(DB_URL, pool_recycle=10, pool_size=25, max_overflow=15)

SessionLocal = scoped_session(sessionmaker(
    bind=engine, autocommit=False, autoflush=False))

SessionLocalLog = scoped_session(sessionmaker(
    bind=engine, autocommit=False, autoflush=False))


Base = declarative_base()


def get_db():
    """get_db for fastapi"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
