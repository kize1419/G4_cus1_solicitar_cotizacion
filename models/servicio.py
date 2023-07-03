from utils.db import db
from dataclasses import dataclass
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

@dataclass
class Servicio(db.Model):
    __tablename__ = 'servicio'
    id_servicio: int
    descripcion: str
    
    id_servicio = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50))
    
    def __init__(self, descripcion):
        self.descripcion = descripcion

class ServicioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Servicio
        include_relationships = True  # para que sus hijos de la clase tambien lo hereden
        load_instance = True  # Para que se puede desSerializar