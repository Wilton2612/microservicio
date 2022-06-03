from utils.db import db



class Reserva(db.Model):
    mentor = db.Column(db.String(20))
    estudiante = db.Column(db.String(20), primary_key=True)
    tipo = db.Column(db.String(20))
    fecha = db.Column(db.Date)

    def __init__(self, mentor, estudiante, tipo, fecha):
        self.mentor = mentor
        self.estudiante= estudiante
        self.tipo = tipo
        self.fecha = fecha

    def toDict(self):
        return dict(mentor=self.mentor, estudiante=self.estudiante, tipo=self.tipo, fecha=self.fecha )
    
    
