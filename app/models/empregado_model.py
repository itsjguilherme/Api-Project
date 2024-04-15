from sqlalchemy import  Column, Integer, String, Numeric, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class Empregado(Base):
    __tablename__ ="employee"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    salary = Column(Numeric)
    birth = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    vehicles = relationship("Vehicle", back_populates="employee")

    def __init__(self, name, email, salary, birth, address):
        self.name = name
        self.email = email
        self.salary =  salary
        self.birth = birth
        self.address = address

    def to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "salary": self.salary,
            "birth": self.birth,
            "address": self.address
        }

        return data
    
    def relationship_to_dict(self):
        data = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "salary": self.salary,
            "birth": self.birth,
            "address": self.address
        }

        return data

    def __repr__(self):
        return f"<Employee {self.id}, {self.name}, {self.email}, {self.salary}, {self.birth}, {self.address}>"