from datetime import date
from utils.db import db
from dataclasses import dataclass

@dataclass
class Solicitud(db.Model):
    __tablename__ = 'solicitud'
    id_solicitud: int
    id_predio: int
    id_solicitante: int
    id_servicio: int
    area_predio: float
    num_casas: int
    cant_acomunes: int
    area_acomunes:int
    cant_vigilantes: int
    cant_plimpieza: int
    cant_administracion: int
    cant_jardineria: int
    fecha_solicitud: date
    nombre_solicitante: str
        
    id_solicitud = db.Column(db.Integer, primary_key=True)
    id_predio = db.Column(db.Integer)
    id_solicitante = db.Column(db.Integer)
    id_servicio = db.Column(db.Integer)
    area_predio = db.Column(db.Float)
    num_casas = db.Column(db.Integer)
    cant_acomunes = db.Column(db.Integer)
    area_acomunes=db.Column(db.Integer)
    cant_vigilantes = db.Column(db.Integer)
    cant_plimpieza = db.Column(db.Integer)
    cant_administracion = db.Column(db.Integer)
    cant_jardineria = db.Column(db.Integer)
    fecha_solicitud = db.Column(db.Date)
    nombre_solicitante = db.Column(db.String)
    
    def __init__(self, id_predio,id_solicitante,id_servicio, area_predio, 
                 num_casas, cant_acomunes, area_acomunes,cant_vigilantes,cant_plimpieza,cant_administracion,
                 cant_jardineria,fecha_solicitud,nombre_solicitante):
        #self.id_solicitud = id_solicitud
        self.id_predio = id_predio
        self.id_solicitante = id_solicitante
        self.id_servicio = id_servicio
        self.area_predio = area_predio
        self.num_casas = num_casas
        self.cant_acomunes = cant_acomunes
        self.area_acomunes = area_acomunes
        self.cant_vigilantes = cant_vigilantes
        self.cant_plimpieza = cant_plimpieza
        self.cant_administracion = cant_administracion
        self.cant_jardineria = cant_jardineria
        self.fecha_solicitud = fecha_solicitud
        self.nombre_solicitante = nombre_solicitante