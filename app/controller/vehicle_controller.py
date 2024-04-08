from sqlalchemy.orm import Session
from app.models.vehicle_model import Vehicle
from app.schemas.vehicleRequests import CreateVehicle, UpdateVehicle
from app.routers import  paginate, instance_update
from fastapi import Response, HTTPException, status
import json


def get_vehicle(db: Session):
    query = db.query(Vehicle)
    vehicles, output = paginate(query, 1, 10)

    for vehicle in vehicles:
        output["itens"].append(vehicle.to_dict())

    return output


def get_vehicle_by_id(db: Session, vehicle_id: int):
    find_vehicle = db.query(Vehicle).get(vehicle_id)

    if not find_vehicle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle with this id not found")
    
    response = {
        "error": False,
        "vehicle": find_vehicle.to_dict()
    }

    return response


def create_vehicle(db: Session, vehicle: CreateVehicle):
    data = vehicle.model_dump()
    plate = data.get("plate").lower()

    if db.query(Vehicle).filter(Vehicle.plate == plate).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="plate already registered")
    
    newVehicle = Vehicle(
        plate = data.get("plate").lower(),
        model = data.get("model"),
        brand = data.get("brand"),
        color = data.get("color"),
        employee_id = data.get("employee_id")
    )

    db.add(newVehicle)
    
    try:
        db.flush()
        db.commit()
        return {"error": False, "message": "Veiculo criado com sucesso"}
    
    except:
        db.rollback()
        return {"error": True, "message": "database error"}


def remove_vehicle(db: Session, vehicle_id: int):
    vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()

    if not vehicle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle with this id not found")
    
    db.delete(vehicle)
    
    try:
        db.commit()
        return Response(json.dumps({"error": False, "message": "veiculo deletado com sucesso"}))

    except:
        db.rollback()
        return Response(json.dumps({"error": True, "message": "database error"}))


def update_vehicle(db: Session, vehicle_id: int, vehicle: UpdateVehicle):
    data = vehicle.model_dump()

    vehicle = db.query(Vehicle).get(vehicle_id)

    if not vehicle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle with this id not found")

    if data.get("plate") is not None:
        lower_plate = data.get("plate").lower()
        repeatedPlate = db.query(Vehicle).filter(Vehicle.plate == lower_plate).first()

        if repeatedPlate:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="plate already registered")

    instance_update(vehicle, data)
    
    try:
        db.commit()
        return {"error": False, "message": "veiculo editado com sucesso"}
    
    except:
        db.rollback()
        return {"error": True, "message": "database error"}