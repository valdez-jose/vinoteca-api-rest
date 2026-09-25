
from pydantic import BaseModel


class VinoCreate(BaseModel):
    nombre: str
    cepa: str
    anio: int
    precio: float
    stock: int = 0
    descripcion: str | None = None
    imagen_url: str | None = None

class VinoUpdate(BaseModel):
    nombre: str | None = None
    cepa: str | None = None
    anio: int | None = None
    precio: float | None = None
    stock: int | None = None
    descripcion: str | None = None
    imagen_url: str | None = None