
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.vino import Vino
from app.schemas.vino import VinoCreate, VinoUpdate


router = APIRouter()


def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Obtener todos los vinos
@router.get("/vinos")
def obtener_vinos(db: Session = Depends(obtener_db)):
    return db.query(Vino).all()

# Obtener un vino por ID
@router.get("/vinos/{vino_id}")
def obtener_vino(vino_id: int, db: Session = Depends(obtener_db)):
    return db.query(Vino).filter(Vino.id == vino_id).first()

# Crear un nuevo vino
@router.post("/vinos")
def crear_vino(vino: VinoCreate, db: Session = Depends(obtener_db)):
    nuevo_vino = Vino(**vino.model_dump())

    db.add(nuevo_vino)
    db.commit()
    db.refresh(nuevo_vino)

    return nuevo_vino

# Actualizar un vino
@router.patch("/vinos/{vino_id}")
def actualizar_vino(
    vino_id: int,
    vino: VinoUpdate,
    db: Session = Depends(obtener_db)
):
    vino_db = db.query(Vino).filter(Vino.id == vino_id).first()

    if vino_db is None:
        return {"mensaje": "Vino no encontrado"}

    datos = vino.model_dump(exclude_unset=True)

    for campo, valor in datos.items():
        setattr(vino_db, campo, valor)

    db.commit()
    db.refresh(vino_db)

    return vino_db

    # Eliminar un vino
@router.delete("/vinos/{vino_id}")
def eliminar_vino(vino_id: int, db: Session = Depends(obtener_db)):
    vino_db = db.query(Vino).filter(Vino.id == vino_id).first()

    if vino_db is None:
        return {"mensaje": "Vino no encontrado"}

    db.delete(vino_db)
    db.commit()

    return {"mensaje": "Vino eliminado correctamente"}