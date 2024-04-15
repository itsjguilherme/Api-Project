from pydantic import BaseModel
from typing import Optional


class CreateVehicle(BaseModel):
    plate: str
    model: str
    brand: str
    color: str
    employee_id: int


class UpdateVehicle(BaseModel):
    plate: Optional[str] = None
    model: Optional[str] = None
    brand: Optional[str] = None
    color: Optional[str] = None
    employee_id: Optional[int] = None
