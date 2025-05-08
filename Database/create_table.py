from dotenv import load_dotenv
import os

load_dotenv()

from database import engine
from models import Base
from loguru import logger

def create_tables():
    logger.info("Creating all tables in the database...")
    Base.metadata.create_all(bind=engine)
    logger.success("All tables created successfully.")

if __name__ == "__main__":
    create_tables()
