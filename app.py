from flask_restful import Api
from Resource.random_resource import CreateRandom, GetReport, Download
from flask import Flask
from Models.random_models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///random.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'kjgfdtfvhgvcfxfsxs122323ffcgcccdcdmnnn'

api = Api(app)
db.init_app(app)


api.add_resource(CreateRandom, "/api/generate/")
api.add_resource(Download, '/api/download/<int:file_id>')
api.add_resource(GetReport, '/api/report/<int:file_id>')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)
