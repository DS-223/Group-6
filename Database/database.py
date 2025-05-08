import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm
from dotenv import load_dotenv
import os

from dotenv import load_dotenv
from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).resolve().parents[2] / ".env")

DATABASE_URL = os.environ.get("DATABASE_URL")

engine = sql.create_engine(DATABASE_URL)

Base = declarative.declarative_base()

SessionLocal = orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()