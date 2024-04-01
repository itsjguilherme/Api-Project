from sqlalchemy import  Column, Integer, String, Numeric
from Database.connection import Base

class Empregado(Base):
    __tablename__ ="employee"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    salary = Column(Numeric)
    birth = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)