from pydantic import BaseModel
from app.swagger_models.generalResponses import PaginationDoc, ResponseEmpregadoGeneric


class ResponseVehicle(BaseModel):
    id: int
    plate: str
    model: str
    brand: str
    color: str
    employee: ResponseEmpregadoGeneric

class VehicleAll(BaseModel):
    error: bool = False
    itens: "list[ResponseVehicle]"
    pagination: PaginationDoc

class VehicleView(BaseModel):
    vehicle: ResponseVehicle
    error: bool