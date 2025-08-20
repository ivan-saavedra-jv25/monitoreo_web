from datetime import datetime
from database import db

class Website(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False, unique=True)
    titular = db.Column(db.String(255), nullable=True)
    fecha_creacion = db.Column(db.String(50), nullable=True)
    fecha_expiracion = db.Column(db.String(50), nullable=True)
    estado = db.Column(db.Integer, nullable=True)
    latency_ms = db.Column(db.Float, nullable=True)
    checked_at = db.Column(db.DateTime, default=datetime.utcnow)
