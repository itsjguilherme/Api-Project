from fastapi import APIRouter, Depends
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.empregadoRequests import CreateEmpregado, UpdateEmpregado
from app.swagger_models.generalResponses import DefaultReponseDoc
from app.swagger_models.employeeResponses import EmployeeAll, EmployeeView

import app.controller.empregado_controller as crud_empregado

router = APIRouter(prefix="/employee", tags=["employee"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creat
@router.post("/add", response_model=DefaultReponseDoc)
async def create_empregado(request: CreateEmpregado, db: Session = Depends(get_db)):
    return crud_empregado.create_empregado(db, empregado=request)


# Read all
@router.get("/all", response_model=EmployeeAll)
async def get_empregado(db: Session = Depends(get_db)):
    _empregados = crud_empregado.get_empregado(db)
    return _empregados


# Read view
@router.get("/view/{empregado_id}", response_model=EmployeeView)
async def get_empregado_by_id(empregado_id: int, db: Session = Depends(get_db)):
    _empregado = crud_empregado.get_empregado_by_id(db, empregado_id=empregado_id)
    return _empregado


# Update
@router.put("/edit", response_model=DefaultReponseDoc)
async def update_empregado(request: UpdateEmpregado, empregado_id: int, db: Session = Depends(get_db)):
    _empregado = crud_empregado.update_empregado(
                            db,
                            empregado_id=empregado_id,
                            empregado=request
                        )
    
    return _empregado


#Delete
@router.delete("/delete/{empregado_id}", response_model=DefaultReponseDoc)
async def delete_empregado(empregado_id: int,  db: Session = Depends(get_db)):
    return crud_empregado.remove_empregado(db, empregado_id=empregado_id)