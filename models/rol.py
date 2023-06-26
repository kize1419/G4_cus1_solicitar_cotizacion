from utils.db import db
from dataclasses import dataclass

@dataclass
class Rol(db.Model):
    __tablename__ = 'rol'
    id_rol:int
    descripcion:str
    
    id_rol=db.Column(db.Integer, primary_key=True)
    descripcion=db.Column(db.String(60))
    
    def __init__(self,descripcion):
        #self.id_rol=id_rol
        self.descripcion=descripcion