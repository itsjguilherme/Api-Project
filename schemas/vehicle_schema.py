from pydantic import BaseModel , Field

class VehicleSchema(BaseModel):
    plate: str
    model: str
    brand: str
    color: str
    employee_id: int

    class Config:
        orm_mode = True

class RequestVehicle(BaseModel):
    parameter: VehicleSchema = Field(...)

class ResponseVehicle(BaseModel):
    plate: str
    model: str
    brand: str
    color: str
    employee_id: int