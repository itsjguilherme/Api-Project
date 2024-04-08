from fastapi import FastAPI
import app.models.empregado_model as models
from app.routers import employee, vehicle
from app.database import Base, engine
import uvicorn

app = FastAPI(title="API Project", description="An API project for studying API developments.")

app.include_router(employee.router)
app.include_router(vehicle.router)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app, port=8001)