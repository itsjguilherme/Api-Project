from sqlalchemy import  Column, Integer, String, Numeric, ForeignKey
from Database.connection import Base
from sqlalchemy.orm import relationship

class Empregado(Base):
    __tablename__ ="employee"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    salary = Column(Numeric)
    birth = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    vehicles = relationship("Vehicle", back_populates="employee")

class Vehicle(Base):
    __tablename__ ="vehicle"

    id = Column(Integer, primary_key=True, autoincrement=True)
    plate = Column(String(255), nullable=False)
    model = Column(String(255), nullable=False)
    brand = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)
    employee_id = Column(Integer, ForeignKey("employee.id"))
    employee = relationship("Empregado", back_populates="vehicles")