from flask import Flask
from flask_restful import Api
from flask_cors import CORS   # 👈 importar
from database import db
from resources import WebsiteResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

# 👇 habilitar CORS (todas las rutas, todos los orígenes)
# CORS(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})


with app.app_context():
    db.create_all()

# Rutas
# api.add_resource(WebsiteResource, "/websites")

api.add_resource(WebsiteResource, '/websites', '/websites/<int:id>')
if __name__ == "__main__":
    app.run(debug=True)
