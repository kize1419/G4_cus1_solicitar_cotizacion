from utils.db import db
from dataclasses import dataclass

@dataclass
class Servicio(db.Model):
    __tablename__ = 'servicio'
    id_servicio: int
    descripcion: str
    
    id_servicio = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(50))
    
    def __init__(self, descripcion):
        self.descripcion = descripcion