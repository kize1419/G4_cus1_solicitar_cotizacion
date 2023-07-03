from utils.db import db
from dataclasses import dataclass
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

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

class SolicitanteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Solicitante
        include_relationships = True #para que sus hijos de la clase tambien lo hereden
        load_instance =True #Para que se puede desSerializar