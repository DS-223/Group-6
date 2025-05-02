from sqlalchemy import create_engine
from app.models.models import Base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created successfully.")

if __name__ == "__main__":
    init_db()
