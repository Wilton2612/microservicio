from flask import Flask
from routes.reservas import reservas
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:lavida1234@localhost/microservicio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

SQLAlchemy(app)
    

app.register_blueprint(reservas)





