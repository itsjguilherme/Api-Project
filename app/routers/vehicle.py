from fastapi import APIRouter, status, Depends
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.vehicleRequests import CreateVehicle, UpdateVehicle
from app.swagger_models.generalResponses import DefaultReponseDoc
from app.swagger_models.vehicleResponses import VehicleAll, VehicleView

import app.controller.vehicle_controller as crud_vehicle

router = APIRouter(prefix="/vehicle", tags=["vehicle"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# VEHICLE_ROUTES

# Creat
@router.post("/create", response_model=DefaultReponseDoc)
async def create_vehicle(request: CreateVehicle, db: Session = Depends(get_db)):
    return crud_vehicle.create_vehicle(db, vehicle=request)


# Read all
@router.get("/all", response_model=VehicleAll)
async def get_vehicle(db: Session = Depends(get_db)):
    _vehicle = crud_vehicle.get_vehicle(db)
    return _vehicle


# Read view
@router.get("/view/{vehicle_id}", response_model=VehicleView)
async def get_vehicle_by_id(vehicle_id: int, db: Session = Depends(get_db)):
    _vehicle = crud_vehicle.get_vehicle_by_id(db, vehicle_id=vehicle_id)
    return _vehicle


# Update
@router.put("/update", response_model=DefaultReponseDoc)
async def update_vehicle(request: UpdateVehicle, vehicle_id: int, db: Session = Depends(get_db)):
    _vehicle = crud_vehicle.update_vehicle(
                            db,
                            vehicle_id=vehicle_id, 
                            vehicle=request
                        )
    return _vehicle


#Delete
@router.delete("/delete/{vehicle_id}", response_model=DefaultReponseDoc)
async def delete_vehicle(vehicle_id: int,  db: Session = Depends(get_db)):
    return crud_vehicle.remove_vehicle(db, vehicle_id=vehicle_id)