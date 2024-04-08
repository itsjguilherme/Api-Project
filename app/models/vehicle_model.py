from sqlalchemy import  Column, Integer, String, Numeric, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship

class Vehicle(Base):
    __tablename__ ="vehicle"

    id = Column(Integer, primary_key=True)
    plate = Column(String(255), nullable=False, unique=True)
    model = Column(String(255), nullable=False)
    brand = Column(String(255), nullable=False)
    color = Column(String(255), nullable=False)
    employee_id = Column(Integer, ForeignKey("employee.id"))
    employee = relationship("Empregado", back_populates="vehicles")

    def __init__(self, plate, model, brand, color, employee_id):
        self.plate = plate
        self.model = model
        self.brand =  brand
        self.color = color
        self.employee_id =  employee_id

    def to_dict(self):
        data = {
            "id": self.id,
            "plate": self.plate,
            "model": self.model,
            "brand": self.brand,
            "color": self.color,
            "employee": self.employee.to_dict(),
        }

        return data

    def __repr__(self):
        return f"<Vehicle {self.id}, {self.plate}, {self.model}, {self.brand}, {self.color}>"