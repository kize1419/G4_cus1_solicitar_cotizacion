from flask import Blueprint, request, jsonify
from models.rol import Rol, RolSchema
from utils.db import db

rol=Blueprint('rol',__name__)
rol_schema = RolSchema()

@rol.route('/rol',methods=['GET'])
def getRol():
    if request.method=='GET':
        data={}
        rol=Rol.query.all()
        #data["rol"]=rol
        return jsonify(rol_schema.dump(rol,many= True))
'''
@rol.route('/rol/add',methods=['POST'])
def addRol():
    data={}
    if request.method=='POST':
        body=request.get_json()
        #id_rol=body['id_rol']
        #descripcion=body['descripcion']
        new_rol=rol_schema.load(body,session=db.session)
        #new_rol= Rol(id_rol,descripcion)
        db.session.add(new_rol)
        db.session.commit()
        #return jsonify(new_rol.dump(new_rol,many=True))
        return rol_schema.jsonify(new_rol)
'''  
@rol.route('/rol/add', methods=['POST'])
def add_rol():
    if request.method == 'POST':
        rol_schema = RolSchema()
        rol_data = request.get_json()
        new_rol = rol_schema.load(rol_data, session=db.session)

        db.session.add(new_rol)
        db.session.commit()

        return jsonify(rol_schema.dump(new_rol))

@rol.route('/rol/update',methods=['POST'])
def updateRol():
    data={}
    body=request.get_json()
    id_rol=body['id_rol']
    rol=Rol.query.get(id_rol)
    if request.method=='POST':
        rol.descripcion=body['descripcion']
        db.session.commit()
    return jsonify(rol)

@rol.route('/rol/delete',methods=['POST'])
def deleteRol():
    data={}
    body=request.get_json()
    id_rol=body['id_rol']
    rol=Rol.query.get(id_rol)
    if request.method=='POST':
        db.session.delete(rol)
        db.session.commit()
    return jsonify(data) 

'''    
@rol.route('/add',methods=['POST'])
def addRol():
    data={}
    if request.method=='POST':
        body=request.get_json()
        description=body['description']
        
        new_rol= Rol(description)
        db.session.add(new_rol)
        db.session.commit()
        return jsonify(data)
        
@rol.route('/update',methods=['POST'])
def updateRol():
    data={}
    body=request.get_json()
    id_rol=body['id_rol']
    rol=Rol.query.get(id_rol)
    if request.method=='POST':
        rol.descripcion=body['descripcion']
        db.session.commit()
    return jsonify(rol)        

@rol.route('/delete',methods=['POST'])
def deleteRol():
    data={}
    body=request.get_json()
    id_rol=body['id_rol']
    rol=Rol.query.get(id_rol)
    if request.method=='POST':
        db.session.delete(rol)
        db.session.commit()
    return jsonify(data)    

'''