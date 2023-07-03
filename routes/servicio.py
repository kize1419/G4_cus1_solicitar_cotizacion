from flask import Blueprint, request, jsonify
from models.servicio import Servicio, ServicioSchema
from utils.db import db


servicio = Blueprint('servicio', __name__)
servicio_schema = ServicioSchema()
@servicio.route('/servicio', methods=['GET'])
def getServicio():
    if request.method == 'GET':
        data = {}
        servicio = Servicio.query.all()
        data["servicio"] = servicio
        return jsonify(servicio_schema.dump(servicio,many=True))

@servicio.route('/add', methods=['POST'])
def addServicio():
    data = {}
    if request.method == 'POST':
        body = request.get_json()
        descripcion = body['descripcion']
        
        new_servicio = Servicio(descripcion)
        db.session.add(new_servicio)
        db.session.commit()
        return jsonify(data)

@servicio.route('/update', methods=['POST'])
def updateServicio():
    data = {}
    body = request.get_json()
    id_servicio = body['id_servicio']
    servicio = Servicio.query.get(id_servicio)
    if request.method == 'POST':
        servicio.descripcion = body['descripcion']
        db.session.commit()
    return jsonify(servicio.to_dict())

@servicio.route('/delete', methods=['POST'])
def deleteServicio():
    data = {}
    body = request.get_json()
    id_servicio = body['id_servicio']
    servicio = Servicio.query.get(id_servicio)
    if request.method == 'POST':
        db.session.delete(servicio)
        db.session.commit()
    return jsonify(data)