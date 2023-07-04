from flask import Blueprint, request, jsonify
from models.personal import Personal, PersonalSchema
from utils.db import db

personal=Blueprint('personal',__name__)
personal_schema = PersonalSchema()

@personal.route('/personal',methods=['GET'])
def getpersonal():
    if request.method=='GET':
        data={}
        personal=Personal.query.all()
        data["personal"]=personal
        # return (data)
        return jsonify(personal_schema.dump(personal,many=True)) #Devolvera la lista de Personal

'''
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
'''
@personal.route('/personal/add', methods=['POST'])
def addpersonal():
    if request.method == 'POST':
        personal_data = request.get_json()
        new_personal = personal_schema.load(personal_data, session=db.session)
        db.session.add(new_personal)
        db.session.commit()

        return jsonify(personal_schema.dump(new_personal))

@personal.route('/update',methods=['POST'])
def updatepersonal():
    data={}
    body=request.get_json()
    id_personal=body['id_rol']
    personal=Personal.query.get(id_personal)
    if request.method=='POST':
        personal.description=body['description']
        db.session.commit()
    return jsonify(personal)        

@personal.route('/delete',methods=['POST'])
def deletepersonal():
    data={}
    body=request.get_json()
    id_personal=body['id_rol']
    personal=Personal.query.get(id_personal)
    if request.method=='POST':
        db.session.delete(personal)
        db.session.commit()
    return jsonify(data)  