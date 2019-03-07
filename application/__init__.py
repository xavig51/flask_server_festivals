from flask import Flask,Blueprint,url_for
from flask_restplus import Api


app=Flask(__name__)

app = Flask(__name__)
blueprint = Blueprint('api', __name__, url_prefix='/application')
api = Api(blueprint,
	title='festivales... a way of life',
	version='v0.1',
	description='servidor api rest',
	doc='/',
	)
app.register_blueprint(blueprint)


from application.festivales.festivalesRest import api as ns1
api.add_namespace(ns1)


