from sqlalchemy import Column, Integer, String, Numeric, Text

from app.database import Base


class Vino(Base):
    __tablename__ = "vinos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True, nullable=False)
    cepa = Column(String, nullable=False)
    anio = Column(Integer, nullable=False)
    precio = Column(Numeric(10, 2), nullable=False)
    stock = Column(Integer, default=0, nullable=False)
    descripcion = Column(Text, nullable=True)
    imagen_url = Column(String, nullable=True)