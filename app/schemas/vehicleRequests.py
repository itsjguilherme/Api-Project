from pydantic import BaseModel
from typing import Optional


class CreateVehicle(BaseModel):
    plate: str
    model: str
    brand: str
    color: str
    employee_id: int

    model_config = {
        "employee_id": 1,
        "plate": "plate",
        "model": "model",
        "brand": "brand",
        "color": "color"
    }

class UpdateVehicle(BaseModel):
    plate: Optional[str] = None
    model: Optional[str] = None
    brand: Optional[str] = None
    color: Optional[str] = None
    employee_id: Optional[int] = None

    model_config = {
        "employee_id": 1,
        "plate": "plate",
        "model": "model",
        "brand": "brand",
        "color": "color"
    }