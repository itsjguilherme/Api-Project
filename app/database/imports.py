from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

STAGE = os.getenv("STAGE", None)

# Localhost: Morticia
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Joao1234@localhost:5432/empresa")

if STAGE == "test":
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:Joao1234@localhost:5432/empresa_test")

# Localhost: Lia
# DATABASE_URL = 'postgresql://postgres:joao1234@localhost:5432/api_empresa'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush = False, bind=engine)
Base = declarative_base()

def get_db():
    def _get_db():
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()
    
    return next(_get_db())