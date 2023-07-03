from datetime import date
from utils.db import db
from dataclasses import dataclass
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

@dataclass
class Personal(db.Model):
    __tablename__ = 'personal'
    id_rol:int
    id_personal:int
    id_persona:int
    fecha_contrato:date
    fecha_cese:date
    
    id_rol=db.Column(db.Integer, primary_key=True)
    id_personal=db.Column(db.Integer)
    id_persona=db.Column(db.Integer)
    fecha_contrato=db.Column(db.Date)
    fecha_cese=db.Column(db.Date)
    
    def __init__(self,id_rol,id_personal,id_persona,fecha_contrato,fecha_cese):
        self.id_rol=id_rol
        self.id_personal=id_personal
        self.id_persona=id_persona
        self.fecha_contrato=fecha_contrato
        self.fecha_cese=fecha_cese

#Serializacion con Marshmallow
class PersonalSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Personal
        include_relationships = True #para que sus hijos de la clase tambien lo hereden
        load_instance =True #Para que se puede desSerializar