from flask import Blueprint, render_template, request, redirect
from models.reserva import Reserva
from utils.db import db
import re


reservas = Blueprint('reservas', __name__)


@reservas.route("/")
def home():
    return render_template('index.html')


@reservas.route('/add', methods=['POST'])
def registrar_reserva():
    db.create_all()

    mentor = request.form['mentor']
    estudiante = request.form['estudiante']
    tipo = request.form['tipo']
    fecha = request.form['fecha']
    new_reserva = Reserva(mentor, estudiante, tipo, fecha)

    db.session.add(new_reserva)
    db.session.commit()
    return redirect('/')


@reservas.route('/reservas')
def lista_reservas():
    reservass = Reserva.query.all()
    return render_template("lista.html", reservass=reservass)


@reservas.route("/reservas/<string:mentor>", methods=["GET"])
def buscar_by_mentor(mentor):
    nombre = ['Camilo', 'Gabriel', 'Andres']

    if mentor in nombre:
        
        reservass = db.session.query(Reserva).filter(Reserva.mentor == mentor)
        print(reservass, "solo name")
        return render_template("unico.html", reservass=reservass)
    else:
        print("ocurre un error")    
        return render_template("error.html")
        



    """print(mentor, "##########nombre")
        reservass = Reserva.query.filter(Reserva.mentor==mentor)
        #reservass = Reserva.query.filter(Reserva.mentor == mentor)
        # reservass = db.session.query(Reserva).filter(Reserva.mentor == mentor[0])
        
        print(reservass, "holaa")    
        return render_template("unico.html", reservass=reservass)"""