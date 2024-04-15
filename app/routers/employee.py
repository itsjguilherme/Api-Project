from fastapi import APIRouter
from app.adapters.employee_adapter import EmployeeAdapter
from app.swagger_models.empregadoRequests import CreateEmpregado, UpdateEmpregado
from app.swagger_models.generalResponses import DefaultReponseDoc
from app.swagger_models.employeeResponses import EmployeeAll, EmployeeView

router = APIRouter(prefix="/employee", tags=["employee"])


# Creat
@router.post("/add", response_model=DefaultReponseDoc)
async def create_empregado(request: CreateEmpregado):
    return EmployeeAdapter().create_empregado(request)


# Read all
@router.get("/all", response_model=EmployeeAll)
async def get_empregado():
    return EmployeeAdapter().get_empregado()


# Read view
@router.get("/view/{empregado_id}", response_model=EmployeeView)
async def get_empregado_by_id(empregado_id: int):
    return EmployeeAdapter().get_empregado_by_id(empregado_id)


# Update
@router.put("/edit", response_model=DefaultReponseDoc)
async def update_empregado(request: UpdateEmpregado, empregado_id: int):
    return EmployeeAdapter().update_empregado(empregado_id, request)


#Delete
@router.delete("/delete/{empregado_id}", response_model=DefaultReponseDoc)
async def delete_empregado(empregado_id: int):
    return EmployeeAdapter().remove_empregado(empregado_id)