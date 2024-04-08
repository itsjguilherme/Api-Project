from pydantic import BaseModel
from typing import Optional


class CreateEmpregado(BaseModel):
    name: str
    email: str
    salary: float
    birth: str
    address: str

    model_config = {
        "name": "employee",
        "email": "employee@email.com",
        "salary": 000.00,
        "birth": "dd/mm/aaaa",
        "address": "address"
    }

class UpdateEmpregado(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    salary: Optional[float] = None
    birth: Optional[str] = None
    address: Optional[str] = None

    model_config = {
        "name": "employee",
        "email": "employee@email.com",
        "salary": 1000.00,
        "birth": "dd/mm/aaaa",
        "address": "address"
    }