from flask import Blueprint, request, jsonify
from models.personal import Personal
from utils.db import db

personal=Blueprint('personal',__name__)

@personal.route('/personal',methods=['GET'])
def getpersonal():
    if request.method=='GET':
        data={}
        personal=Personal.query.all()
        data["personal"]=personal
        return jsonify(data)

@personal.route('/personal/add',methods=['POST'])
def addpersonal():
    data={}
    if request.method=='POST':
        body=request.get_json()
        description=body['description']
        
        new_personal= personal(description)
        db.session.add(new_personal)
        db.session.commit()
        return jsonify(data)
    
@personal.route('/update',methods=['POST'])
def updatepersonal():
    data={}
    body=request.get_json()
    id_personal=body['id_rol']
    personal=personal.query.get(id_personal)
    if request.method=='POST':
        personal.description=body['description']
        db.session.commit()
    return jsonify(personal)        

@personal.route('/delete',methods=['POST'])
def deletepersonal():
    data={}
    body=request.get_json()
    id_personal=body['id_rol']
    personal=personal.query.get(id_personal)
    if request.method=='POST':
        db.session.delete(personal)
        db.session.commit()
    return jsonify(data)  