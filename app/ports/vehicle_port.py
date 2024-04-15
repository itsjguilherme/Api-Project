from app.services.vehicle_service import VehicleService

class VehiclePort:
    def __init__(self) -> None:
        pass

    def get_vehicle(self):
        return VehicleService().get_vehicle()
    
    def get_vehicle_by_id(self, vehicle_id):
        return VehicleService().get_vehicle_by_id(vehicle_id)
    
    def create_vehicle(self, vehicle):
        return VehicleService().create_vehicle(vehicle)
    
    def update_vehicle(self, vehicle_id, vehicle):
        return VehicleService().update_vehicle(vehicle_id, vehicle)
    
    def remove_vehicle(self, vehicle_id):
        return VehicleService().remove_vehicle(vehicle_id)