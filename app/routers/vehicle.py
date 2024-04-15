from fastapi import APIRouter
from app.adapters.vehicle_adapter import VehicleAdapter
from app.swagger_models.vehicleRequests import CreateVehicle, UpdateVehicle
from app.swagger_models.generalResponses import DefaultReponseDoc
from app.swagger_models.vehicleResponses import VehicleAll, VehicleView

router = APIRouter(prefix="/vehicle", tags=["vehicle"])


# VEHICLE_ROUTES

# Creat
@router.post("/create", response_model=DefaultReponseDoc)
async def create_vehicle(request: CreateVehicle):
    return VehicleAdapter().create_vehicle(request)


# Read all
@router.get("/all", response_model=VehicleAll)
async def get_vehicle():
    return VehicleAdapter().get_vehicle()


# Read view
@router.get("/view/{vehicle_id}", response_model=VehicleView)
async def get_vehicle_by_id(vehicle_id: int):
    return VehicleAdapter().get_vehicle_by_id(vehicle_id)


# Update
@router.put("/update", response_model=DefaultReponseDoc)
async def update_vehicle(request: UpdateVehicle, vehicle_id: int):
    return VehicleAdapter().update_vehicle(vehicle_id, request)


#Delete
@router.delete("/delete/{vehicle_id}", response_model=DefaultReponseDoc)
async def delete_vehicle(vehicle_id: int):
    return VehicleAdapter().remove_vehicle(vehicle_id)