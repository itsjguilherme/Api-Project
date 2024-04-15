from pydantic import BaseModel
from typing import Optional


class CreateEmpregado(BaseModel):
    name: str
    email: str
    salary: float
    birth: str
    address: str


class UpdateEmpregado(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    salary: Optional[float] = None
    birth: Optional[str] = None
    address: Optional[str] = None
