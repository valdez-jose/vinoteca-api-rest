
from fastapi import FastAPI
from app.database import Base, engine
from app.models.vino import Vino
from app.routers import vinos

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(vinos.router)


@app.get("/")
def inicio():
    return {"mensaje": "API Vinoteca funcionando"}