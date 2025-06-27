from datetime import datetime, date
from config import db

class Reserva(db.Model):
    __tablename__ = "reservas"
    
    id= db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date, nullable=False)
    hora_inicio = db.Column(db.Time, nullable=False) # A coluna usa db.Time, então o SQLite armazena o horário no formato HH:MM:SS.ssssss
    hora_fim = db.Column(db.Time, nullable=False)
    turma_id = db.Column(db.Integer, nullable=False)
    sala = db.Column(db.String(10), nullable=False)
    
    def __init__(self, data, hora_inicio, hora_fim, turma_id,sala):
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.turma_id = turma_id
        self.sala = sala
    
    def to_dict(self):
        return {
            'id': self.id,
            'data': self.data.strftime('%Y-%m-%d'),
            'hora_inicio': self.hora_inicio.strftime('%H:%M'),
            'hora_fim': self.hora_fim.strftime('%H:%M'),
            'turma_id': self.turma_id,
            'sala': self.sala
        }
        
class TurmaNaoEncontrada(Exception):
    pass