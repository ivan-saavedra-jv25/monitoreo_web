# Monitoreo Web

Este proyecto es una aplicación de monitoreo de sitios web y dominios, que permite consultar el estado, titularidad y fechas de expiración/creación de dominios, así como la latencia de respuesta de los sitios. Incluye un backend en Python (Flask) y un frontend en React.

## Características

- Consulta de estado HTTP y latencia de sitios web.
- Consulta de información de dominios nacionales (.cl) y no nacionales.
- Visualización de resultados en una tabla interactiva.
- Agregar y eliminar sitios a monitorear.
- Indicadores visuales de estado (círculo verde/rojo).
- Panel de control con métricas de sitios activos, inactivos y totales.

## Tecnologías utilizadas

- **Backend:** Python, Flask, Flask-RESTful, SQLAlchemy, requests, BeautifulSoup, tldextract, whois
- **Frontend:** React, Bootstrap
- **Base de datos:** SQLite (puedes cambiarla por otra compatible con SQLAlchemy)

## Estructura del proyecto

```
monitoreo_web/
│
├── backend/
│   ├── consulta_web.py      # Lógica de consulta y parsing de dominios/sitios
│   ├── resources.py         # Endpoints RESTful para sitios web
│   ├── models.py            # Modelos de base de datos
│   ├── database.py          # Configuración de la base de datos
│   └── app.py               # Inicialización de la app Flask
│
├── dashboard-app/
│   └── src/
│       ├── components/
│       │   └── Table.js     # Tabla de visualización de sitios
│       ├── pages/
│       │   └── Dashboard.js # Página principal del dashboard
│       └── App.js           # Entrada principal de React
│
└── README.md
```

## Instalación

### Backend

1. Ve a la carpeta `backend`:
   ```bash
   cd monitoreo_web/backend
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Inicia el servidor Flask:
   ```bash
   flask run
   ```

### Frontend

1. Ve a la carpeta `dashboard-app`:
   ```bash
   cd monitoreo_web/dashboard-app
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Inicia la aplicación React:
   ```bash
   npm start
   ```

## Uso

- Accede al dashboard en [http://localhost:3000](http://localhost:3000).
- Agrega una URL o IP para monitorear.
- Elimina sitios desde la tabla.
- Visualiza el estado, titular, fechas y latencia de cada sitio.

## API

- **GET /websites**: Lista todos los sitios monitoreados.
- **POST /websites**: Agrega o actualiza un sitio. JSON esperado: `{ "url": "https://ejemplo.cl" }`
- **DELETE /websites/<id>**: Elimina un sitio por ID.

## Notas

- El backend debe estar corriendo para que el frontend funcione correctamente.
- Puedes adaptar la base de datos y los endpoints según tus necesidades.

---

**Desarrollado por:**