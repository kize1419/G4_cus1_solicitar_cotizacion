from utils.db import db
from dataclasses import dataclass
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

@dataclass
class Rol(db.Model):
    __tablename__ = 'rol'
    id_rol:int
    descripcion:str
    
    id_rol=db.Column(db.Integer, primary_key=True)
    descripcion=db.Column(db.String(60))
    
    def __init__(self,id_rol,descripcion):
        self.id_rol=id_rol
        self.descripcion=descripcion

class RolSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Rol
        include_relationships = True #para que sus hijos de la clase tambien lo hereden
        load_instance =True #Para que se puede desSerializar