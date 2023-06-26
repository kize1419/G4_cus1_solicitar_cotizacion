from utils.db import db
from dataclasses import dataclass

@dataclass
class Solicitante(db.Model):
    __tablename__ = 'solicitante'
    id_solicitante: int
    id_rol: int
    id_persona: int
    telefono: int
    correo: str
    
    id_solicitante = db.Column(db.Integer, primary_key=True)
    id_rol = db.Column(db.Integer)
    id_persona = db.Column(db.Integer)
    telefono = db.Column(db.Integer)
    correo = db.Column(db.String)
    
    def __init__(self, id_rol, id_persona, telefono,correo):
        self.id_rol = id_rol
        self.id_persona = id_persona
        self.telefono = telefono
        self.correo = correo