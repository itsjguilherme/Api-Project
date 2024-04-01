from pydantic import BaseModel , Field


class EmpregadoSchema(BaseModel):
    id : int
    name : str
    email : str
    salary : float
    birth : str
    address : str

    class Config:
        orm_mode = True


class RequestEmpregado(BaseModel):
    parameter: EmpregadoSchema = Field(...)


class ResponseEmpregado(BaseModel):
    id : int
    name : str
    email : str
    salary : float
    birth : str
    address : str
    code: str
    status: str
    message: str