from flask import request, jsonify
from flask_restful import Resource
from database import db
from models import Website
from consulta_web import obtener_info_web, consulta_web
from datetime import datetime
import re


def clean_and_format_date(value):

    if value is None:
        return None
    return f"{value}"[0:10]
   
    
class WebsiteResource(Resource):

    
    def get(self):
        websites = Website.query.all()
        data = []
        for w in websites:
            data.append({
            "id": w.id,
            "url": w.url,
            "titular": w.titular,
            "fecha_creacion": clean_and_format_date(w.fecha_creacion),
            "fecha_expiracion": clean_and_format_date(w.fecha_expiracion),
            "estado": w.estado,
            "latency_ms": w.latency_ms,
            "checked_at": clean_and_format_date(w.checked_at)
        })
        return jsonify(data)

    def post(self):
        payload = request.get_json()
        url = payload.get("url")
        if not url:
            return jsonify({"error": "Se requiere la URL"}), 400

        # Obtenemos la información con tu función
        info = obtener_info_web(url)

       # Si info es None, usamos un diccionario vacío
        info = info or {}

        consulta_fecha = info.get("consulta_fecha_nacional") or {}
        consulta_web = info.get("consulta_web") or {}

        clean_data = {
            "url": info.get("url"),
            "titular": consulta_fecha.get("Titular"),
            "fecha_creacion": consulta_fecha.get("Fecha_de_creacion"),
            "fecha_expiracion": consulta_fecha.get("Fecha_de_expiracion"),
            "estado": consulta_web.get("status_code"),
            "latency_ms": consulta_web.get("latency_ms")
        }


        # Verificamos si la URL ya existe
        website = Website.query.filter_by(url=clean_data["url"]).first()
        if website:
            # Actualizamos los campos
            website.titular = clean_data["titular"]
            website.fecha_creacion = clean_data["fecha_creacion"]
            website.fecha_expiracion = clean_data["fecha_expiracion"]
            website.estado = clean_data["estado"]
            website.latency_ms = clean_data["latency_ms"]
            website.checked_at = datetime.utcnow()
        else:
            website = Website(**clean_data)
            db.session.add(website)

        db.session.commit()

        return jsonify({"message": "Website added/updated", "id": website.id, "data": clean_data})

    def delete(self, id):
            website = Website.query.get(id)
            if not website:
                return jsonify({"error": "No existe el registro con ese id"}), 404

            db.session.delete(website)
            db.session.commit()
            return jsonify({"message": f"Website con id {id} eliminado correctamente"})
    
    def put(self):
        websites = Website.query.all()
        data = []
        for w in websites:
            print(w)
            info = consulta_web(w.url)
            info = info or {}
            
            w.estado = info.get("status_code")
            w.latency_ms = info.get("latency_ms")
            w.checked_at = datetime.utcnow()
            db.session.commit()
            data.append({
                "id": w.id,
                "url": w.url,
                "titular": w.titular,
                "fecha_creacion": clean_and_format_date(w.fecha_creacion),
                "fecha_expiracion": clean_and_format_date(w.fecha_expiracion),
                "estado": w.estado,
                "latency_ms": w.latency_ms,
                "checked_at": clean_and_format_date(w.checked_at)
            })
        return jsonify(data)

            

            
            
            