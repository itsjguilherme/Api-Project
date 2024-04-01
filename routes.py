from fastapi import APIRouter, HTTPException, status, Depends
from Database.connection import SessionLocal
from sqlalchemy.orm import Session
from schemas.empregado_schema import ResponseEmpregado, RequestEmpregado

import Controller.empregado_controller as crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Creat
@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_empregado(empregado_id: int, request: RequestEmpregado, db: Session = Depends(get_db)):
    crud.create_empregado(db, empregado=request.parameter, empregado_id=empregado_id)


# Read all
@router.get("/all", status_code=status.HTTP_200_OK)
async def get_empregado(db: Session = Depends(get_db)):
    _empregados = crud.get_empregado(db)
    return _empregados


# Read view
@router.get("/view/{empregado_id}", status_code=status.HTTP_200_OK)
async def get_empregado_by_id(empregado_id: int, db: Session = Depends(get_db)):
    _empregados = crud.get_empregado_by_id(db, empregado_id=empregado_id)
    return _empregados


# Update
@router.put("/update")
async def update_empregado(request: RequestEmpregado, db: Session = Depends(get_db)):
    _empregado = crud.update_empregado(
                            db,
                            empregado_id=request.parameter.id, 
                            name=request.parameter.name,
                            email=request.parameter.email,
                            salary=request.parameter.salary,
                            birth=request.parameter.birth,
                            address=request.parameter.address
                        )


#Delete
@router.delete("/delete/{empregado_id}")
async def delete_empregado(empregado_id: int,  db: Session = Depends(get_db)):
    crud.remove_empregado(db, empregado_id=empregado_id)