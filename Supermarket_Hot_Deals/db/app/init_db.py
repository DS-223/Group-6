from sqlalchemy import create_engine
from app.models.models import Base

from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:admin1234@localhost:5432/supermarket_hot_deals_db"

engine = create_engine(DATABASE_URL)

engine = create_engine(DATABASE_URL)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created successfully.")

if __name__ == "__main__":
    init_db()
