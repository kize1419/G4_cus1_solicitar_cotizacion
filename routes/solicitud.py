from flask import Blueprint, request, jsonify
from models.solicitud import Solicitud
from utils.db import db

solicitud = Blueprint('solicitud', __name__)

@solicitud.route('/solicitud', methods=['GET'])
def getSolicitud():
    if request.method == 'GET':
        data = {}
        solicitud = Solicitud.query.all()
        data["solicitud"] = solicitud
        return jsonify(data)
    
    
'''
@solicitud.route('/add', methods=['POST'])
def addSolicitud():
    data = {}
    if request.method == 'POST':
        body = request.get_json()
        id_solicitante = body['id_solicitante']
        id_tipo_predio = body['id_tipo_predio']
        id_servicio = body['id_servicio']
        ruc = body['ruc']
        nombre_predio = body['nombre_predio']
        region = body['region']
        direccion = body['direccion']
        area = body['area']
        cantidad_casas = body['cantidad_casas']
        cantidad_areas_comunes = body['cantidad_areas_comunes']
        cantidad_vigilantes = body['cantidad_vigilantes']
        cantidad_personal_limpieza = body['cantidad_personal_limpieza']
        
        new_solicitud = Solicitud(id_solicitante=id_solicitante, id_tipo_predio=id_tipo_predio, id_servicio=id_servicio,
                                  ruc=ruc, nombre_predio=nombre_predio, region=region, direccion=direccion,
                                  area=area, cantidad_casas=cantidad_casas, cantidad_areas_comunes=cantidad_areas_comunes,
                                  cantidad_vigilantes=cantidad_vigilantes,
                                  cantidad_personal_limpieza=cantidad_personal_limpieza)
        db.session.add(new_solicitud)
        db.session.commit()
        return jsonify(data)

@solicitud.route('/update', methods=['POST'])
def updateSolicitud():
    data = {}
    body = request.get_json()
    id_solicitud = body['id_solicitud']
    solicitud = Solicitud.query.get(id_solicitud)
    if request.method == 'POST':
        solicitud.id_solicitante = body['id_solicitante']
        solicitud.id_tipo_predio = body['id_tipo_predio']
        solicitud.id_servicio = body['id_servicio']
        solicitud.ruc = body['ruc']
        solicitud.nombre_predio = body['nombre_predio']
        solicitud.region = body['region']
        solicitud.direccion = body['direccion']
        solicitud.area = body['area']
        solicitud.cantidad_casas = body['cantidad_casas']
        solicitud.cantidad_areas_comunes = body['cantidad_areas_comunes']
        solicitud.cantidad_vigilantes = body['cantidad_vigilantes']
        solicitud.cantidad_personal_limpieza = body['cantidad_personal_limpieza']
        db.session.commit()
    return jsonify(solicitud.to_dict())

@solicitud.route('/delete', methods=['POST'])
def deleteSolicitud():
    data = {}
    body = request.get_json()
    id_solicitud = body['id_solicitud']
    solicitud = Solicitud.query.get(id_solicitud)
    if request.method == 'POST':
        db.session.delete(solicitud)
        db.session.commit()
    return jsonify(data)
    '''