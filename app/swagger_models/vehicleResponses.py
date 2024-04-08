from pydantic import BaseModel
from app.swagger_models.generalResponses import PaginationDoc
from app.swagger_models.employeeResponses import ResponseEmpregado


class ResponseVehicle(BaseModel):
    id: int
    plate: str
    model: str
    brand: str
    color: str
    employee: ResponseEmpregado

class VehicleAll(BaseModel):
    error: bool = False
    itens: "list[ResponseVehicle]"
    pagination: PaginationDoc

class VehicleView(BaseModel):
    vehicle: ResponseVehicle
    error: bool