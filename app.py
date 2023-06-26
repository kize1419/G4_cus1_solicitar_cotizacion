from flask import Flask

from utils.db import db
#from routes.contact import contact
from routes.rol import rol
from routes.servicio import servicio
from routes.personal import personal
from routes.solicitud import solicitud
from routes.solicitante import solicitante
from routes.solicitud_cotizacion import solicitud_cotizacion

from config import DATABASE_CONNECTION

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION
db.init_app(app)
app.register_blueprint(rol)
app.register_blueprint(personal)
app.register_blueprint(servicio)
app.register_blueprint(solicitante)
app.register_blueprint(solicitud_cotizacion)
app.register_blueprint(solicitud)


#app.register_blueprint(contact)

if __name__=="__main__":
    app.run(debug=True)
