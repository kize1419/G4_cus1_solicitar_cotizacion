from flask import Blueprint, request, jsonify
from models.solicitud_cotizacion import Solicitud_Cotizacion
from utils.db import db

solicitud_cotizacion = Blueprint('solicitud_cotizacion', __name__)

@solicitud_cotizacion.route('/solicitud_cotizacion', methods=['GET'])
def getSolicitud_Cotizacion():
    if request.method == 'GET':
        data = {}
        solicitud_cotizacion = Solicitud_Cotizacion.query.all()
        data["solicitud_cotizacion"] = solicitud_cotizacion
        return jsonify(data)

@solicitud_cotizacion.route('/add', methods=['POST'])
def addSolicitud_Cotizacion():
    data = {}
    if request.method == 'POST':
        body = request.get_json()
        id_personal = body['id_personal']
        id_solicitante = body['id_solicitante']
        id_solicitud = body['id_solicitud']
        
        new_solicitud_cotizacion = Solicitud_Cotizacion(id_personal=id_personal, id_solicitante=id_solicitante,
                                                      id_solicitud=id_solicitud)
        db.session.add(new_solicitud_cotizacion)
        db.session.commit()
        return jsonify(data)

@solicitud_cotizacion.route('/update', methods=['POST'])
def updateSolicitud_Cotizacion():
    data = {}
    body = request.get_json()
    id_solicitud_cotizacion = body['id_solicitud_cotizacion']
    solicitud_cotizacion = Solicitud_Cotizacion.query.get(id_solicitud_cotizacion)
    if request.method == 'POST':
        solicitud_cotizacion.id_personal = body['id_personal']
        solicitud_cotizacion.id_solicitante = body['id_solicitante']
        solicitud_cotizacion.id_solicitud = body['id_solicitud']
        db.session.commit()
    return jsonify(solicitud_cotizacion.to_dict())

@solicitud_cotizacion.route('/delete', methods=['POST'])
def deleteSolicitud_Cotizacion():
    data = {}
    body = request.get_json()
    id_solicitud_cotizacion = body['id_solicitud_cotizacion']
    solicitud_cotizacion = Solicitud_Cotizacion.query.get(id_solicitud_cotizacion)
    if request.method == 'POST':
        db.session.delete(solicitud_cotizacion)
        db.session.commit()
    return jsonify(data)