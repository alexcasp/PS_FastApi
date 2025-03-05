from flask import Flask
from flask_restx import Api
from routes import init_routes

app = Flask(__name__)
api = Api(app, title="Blog API", description="Документация API", doc="/docs")

init_routes(api)

if __name__ == "__main__":
    app.run(debug=True)
