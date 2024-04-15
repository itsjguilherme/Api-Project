from pydantic import BaseModel
from app.swagger_models.generalResponses import PaginationDoc
from app.swagger_models.vehicleResponses import ResponseVehicle


class ResponseEmpregado(BaseModel):
    id : int
    name : str
    email : str
    salary : float
    birth : str
    address : str

class EmployeeAll(BaseModel):
    error: bool = False
    itens: "list[ResponseEmpregado]"
    pagination: PaginationDoc

class EmployeeView(BaseModel):
    employee: ResponseEmpregado
    error: bool