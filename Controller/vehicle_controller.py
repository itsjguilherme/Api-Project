from sqlalchemy.orm import Session
from Models.empregado_model import Vehicle
from schemas.vehicle_schema import VehicleSchema
from fastapi import HTTPException, status


def get_vehicle(db: Session):
    return db.query(Vehicle).all()


def get_vehicle_by_id(db: Session, vehicle_id: int):
    find_vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
    if find_vehicle is not None:
        return find_vehicle
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle with this id not found")


def create_vehicle(db: Session, vehicle: VehicleSchema):
    _vehicle = Vehicle(
        #id = empregado.id,
        plate = vehicle.plate,
        model = vehicle.model,
        brand = vehicle.brand,
        color = vehicle.color,
        employee_id = vehicle.employee_id)

    db.add(_vehicle)
    db.commit()
    db.refresh(_vehicle)
    return _vehicle


def remove_vehicle(db: Session, vehicle_id: int):
    _vehicle = get_vehicle_by_id(db=db, vehicle_id=vehicle_id)
    if _vehicle is not None:
        db.delete(_vehicle)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Vehicle deleted successfully")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle with this id not found")


def update_vehicle(db: Session, vehicle_id: int, plate: str, model: str, brand: str, color: str, employee_id: int):
    _vehicle = get_vehicle_by_id(db=db, vehicle_id=vehicle_id)
    if _vehicle is not None:
        _vehicle.plate = plate
        _vehicle.model = model
        _vehicle.brand = brand
        _vehicle.color = color
        _vehicle.employee_id = employee_id

        db.commit()
        db.refresh(_vehicle)
        return _vehicle
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle with this id not found")