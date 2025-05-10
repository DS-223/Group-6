#from dotenv import load_dotenv
#import os

#load_dotenv()

#from database import engine
#from models import Base
#from loguru import logger

#def create_tables():
#    logger.info("Creating all tables in the database...")
#    Base.metadata.create_all(bind=engine)
#    logger.success("All tables created successfully.")

#if __name__ == "__main__":
#    create_tables()

from dotenv import load_dotenv
import os
import time
import psycopg2
from psycopg2 import OperationalError
from database import engine
from models import Base
from loguru import logger

from pathlib import Path
load_dotenv(dotenv_path=Path("/app/.env"), override=True)

# Environment variables
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def wait_for_postgres():
    max_retries = 10
    retry_delay = 2
    retries = 0

    while retries < max_retries:
        try:
            print(f"🔍 Loaded: {DB_USER}@{DB_HOST}:{DB_PORT} → {DB_NAME}")
            conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=DB_PORT
            )
            conn.close()
            print("✅ PostgreSQL is ready.")
            return
        except OperationalError as e:
            print(f"⏳ Waiting for PostgreSQL... (Attempt {retries + 1})")
            time.sleep(retry_delay)
            retries += 1

    raise Exception("❌ Could not connect to PostgreSQL after several attempts.")

def create_tables():
    logger.info("Creating all tables in the database...")
    Base.metadata.create_all(bind=engine)
    logger.success("All tables created successfully.")

if __name__ == "__main__":
    wait_for_postgres()
    create_tables()

