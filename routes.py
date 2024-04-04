from fastapi import APIRouter, HTTPException, status, Depends
from Database.connection import SessionLocal
from sqlalchemy.orm import Session
from schemas.empregado_schema import ResponseEmpregado, RequestEmpregado
from schemas.vehicle_schema import RequestVehicle

import Controller.empregado_controller as crud_empregado
import Controller.vehicle_controller as crud_vehicle

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# EMPLOYEE_ROUTES

# Creat
@router.post("/employee/create", status_code=status.HTTP_201_CREATED)
async def create_empregado(request: RequestEmpregado, db: Session = Depends(get_db)):
    crud_empregado.create_empregado(db, empregado=request.parameter)


# Read all
@router.get("/employee/all", status_code=status.HTTP_200_OK)
async def get_empregado(db: Session = Depends(get_db)):
    _empregados = crud_empregado.get_empregado(db)
    return _empregados


# Read view
@router.get("/employee/view/{empregado_id}", status_code=status.HTTP_200_OK)
async def get_empregado_by_id(empregado_id: int, db: Session = Depends(get_db)):
    _empregados = crud_empregado.get_empregado_by_id(db, empregado_id=empregado_id)
    return _empregados


# Update
@router.put("/employee/update")
async def update_empregado(request: RequestEmpregado, empregado_id: int, db: Session = Depends(get_db)):
    _empregado = crud_empregado.update_empregado(
                            db,
                            empregado_id=empregado_id, 
                            name=request.parameter.name,
                            email=request.parameter.email,
                            salary=request.parameter.salary,
                            birth=request.parameter.birth,
                            address=request.parameter.address
                        )


#Delete
@router.delete("/employee/delete/{empregado_id}")
async def delete_empregado(empregado_id: int,  db: Session = Depends(get_db)):
    crud_empregado.remove_empregado(db, empregado_id=empregado_id)


# VEHICLE_ROUTES

# Creat
@router.post("/vehicle/create", status_code=status.HTTP_201_CREATED)
async def create_vehicle(request: RequestVehicle, db: Session = Depends(get_db)):
    crud_vehicle.create_vehicle(db, vehicle=request.parameter)


# Read all
@router.get("/vehicle/all", status_code=status.HTTP_200_OK)
async def get_vehicle(db: Session = Depends(get_db)):
    _vehicle = crud_vehicle.get_vehicle(db)
    return _vehicle


# Read view
@router.get("/vehicle/view/{vehicle_id}", status_code=status.HTTP_200_OK)
async def get_vehicle_by_id(vehicle_id: int, db: Session = Depends(get_db)):
    _vehicle = crud_vehicle.get_vehicle_by_id(db, vehicle_id=vehicle_id)
    return _vehicle


# Update
@router.put("/vehicle/update")
async def update_vehicle(request: RequestVehicle, vehicle_id: int, db: Session = Depends(get_db)):
    _vehicle = crud_vehicle.update_vehicle(
                            db,
                            vehicle_id=vehicle_id, 
                            plate=request.parameter.plate,
                            model=request.parameter.model,
                            brand=request.parameter.brand,
                            color=request.parameter.color,
                            employee_id=request.parameter.employee_id
                        )


#Delete
@router.delete("/vehicle/delete/{vehicle_id}")
async def delete_vehicle(vehicle_id: int,  db: Session = Depends(get_db)):
    crud_vehicle.remove_vehicle(db, vehicle_id=vehicle_id)