from datetime import date
from utils.db import db
from dataclasses import dataclass
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

@dataclass
class Solicitud_Cotizacion(db.Model):
    __tablename__ = 'solicitud_cotizacion'
    id_solicitud: int
    id_personal: int
    #id_solicitante: int
    fecha_cotizacion:date
    importe:int
    
    id_solicitud = db.Column(db.Integer, primary_key=True)
    id_personal = db.Column(db.Integer)
    #id_solicitante = db.Column(db.Integer)
    fecha_cotizacion=db.Column(db.Date)
    #id_solicitud = db.Column(db.Integer)
    importe = db.Column(db.Integer)
    
    def __init__(self, id_personal,fecha_cotizacion ,importe):
        self.id_personal = id_personal
        #self.id_solicitante = id_solicitante
        self.fecha_cotizacion=fecha_cotizacion
        #self.id_solicitud = id_solicitud
        self.importe=importe

class Solicitud_CotizacionSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Solicitud_Cotizacion
        include_relationships = True #para que sus hijos de la clase tambien lo hereden
        load_instance =True #Para que se puede desSerializar