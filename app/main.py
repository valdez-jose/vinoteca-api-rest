
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models.vino import Vino
from app.routers import vinos


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
  allow_origins=[
    "http://127.0.0.1:5500",
    "http://localhost:5173",
    "http://localhost:4200",
    "https://vinoteca-react.vercel.app",
],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(vinos.router)


@app.get("/")
def inicio():
    return {"mensaje": "API Vinoteca funcionando"}