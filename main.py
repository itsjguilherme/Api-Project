from fastapi import FastAPI
import Models.empregado_model as models
from routes import router
from Database.connection import engine
import uvicorn

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/empregado", tags=["empregado"])

if __name__ == "__main__":
    uvicorn.run(app, port=8001)