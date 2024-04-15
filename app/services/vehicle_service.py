from sqlalchemy.orm import Session
from app.models.vehicle_model import Vehicle
from app.routers import  paginate, instance_update
from fastapi import Response, HTTPException, status
import json
from app.database import get_db


class VehicleService:
    def __init__(self):
        pass

    def get_vehicle(self):
        db = get_db()
        query = db.query(Vehicle)
        vehicles, output = paginate(query, 1, 10)

        for vehicle in vehicles:
            output["itens"].append(vehicle.to_dict())

        return output


    def get_vehicle_by_id(self, vehicle_id):
        db = get_db()
        find_vehicle = db.query(Vehicle).get(vehicle_id)

        if not find_vehicle:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle with this id not found")
        
        response = {
            "error": False,
            "vehicle": find_vehicle.to_dict()
        }

        return response


    def create_vehicle(self, vehicle):
        db = get_db()
        plate = vehicle.get("plate").lower()

        if db.query(Vehicle).filter(Vehicle.plate == plate).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="plate already registered")
        
        newVehicle = Vehicle(**vehicle)

        db.add(newVehicle)
        
        try:
            db.flush()
            db.commit()
            return {"error": False, "message": "Veiculo criado com sucesso"}
        
        except:
            db.rollback()
            return {"error": True, "message": "database error"}


    def remove_vehicle(self, vehicle_id):
        db = get_db()
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


    def update_vehicle(self, vehicle_id, vehicle):
        db = get_db()
        plate = vehicle.get("plate").lower()

        veiculo = db.query(Vehicle).get(vehicle_id)

        if not vehicle:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vehicle with this id not found")

        if db.query(Vehicle).filter(Vehicle.plate == plate).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="plate already registered")

        instance_update(veiculo, vehicle)
        
        try:
            db.commit()
            return {"error": False, "message": "veiculo editado com sucesso"}
        
        except:
            db.rollback()
            return {"error": True, "message": "database error"}