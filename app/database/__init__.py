from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Localhost: Morticia
DATABASE_URL = 'postgresql://postgres:Joao1234@localhost:5432/empresa'

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