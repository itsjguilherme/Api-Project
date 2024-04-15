from app.ports.vehicle_port import VehiclePort
from app.swagger_models.vehicleRequests import CreateVehicle, UpdateVehicle

class VehicleAdapter:
    def __init__(self) -> None:
        pass

    def get_vehicle(self):
        return VehiclePort().get_vehicle()
    
    def get_vehicle_by_id(self, vehicle_id):
        return VehiclePort().get_vehicle_by_id(vehicle_id)
    
    def create_vehicle(self, vehicle: CreateVehicle):
        data = vehicle.model_dump()
        data['plate'] = data['plate'].lower()

        return VehiclePort().create_vehicle(data)
    
    def update_vehicle(self, vehicle_id, vehicle):
        data = vehicle.model_dump()
        data['plate'] = data['plate'].lower()

        return VehiclePort().update_vehicle(vehicle_id, data)
    
    def remove_vehicle(self, vehicle_id):
        return VehiclePort().remove_vehicle(vehicle_id)