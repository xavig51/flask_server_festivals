from flask import Flask,Blueprint,url_for
from flask_restplus import Api
from flask import request
import json
from pymongo import MongoClient
from flask_restplus import Namespace, Resource,fields,reqparse
from flask_cors import CORS, cross_origin

app = Flask("flask_server")
blueprint = Blueprint('api', __name__, url_prefix='/application')
api = Api(blueprint,
	title='festivales... a way of life',
	version='v0.1',
	description='servidor api rest',
	doc='/',
	)
app.register_blueprint(blueprint)

ns1 = Namespace('festivales',description='servicios de consulta de datos de festivales por país')

def normalizacion(cadena):
	cadena=cadena.replace("\"","").replace("'","").replace(": ","\":\"").replace(", ","\",\"").replace("{","{\"") \
				.replace("}","\"}")
	return cadena.replace("http\":\"","http:").replace("https\":\"","https:")

client = MongoClient('mongodb+srv://cluster0-lhfgs.gcp.mongodb.net/test',username='consulter ' \
	#,password='do5CKIyIyKNvE6BY',connect=False)
	
@ns1.route('/espana')
class consulta(Resource):
	@cross_origin()
	def get(self):
		#return "hello world"
		salida="["
		festivales = client['festivales'].spain
		i=0
		for festival in festivales.find():
			#parcial=str(festival).replace("'),",")\",").replace("ObjectId(\'","\"ObjectId(").replace("\'","\"")
			parcial=normalizacion(str(festival))
			print(str(festival))
			if(i==0):
				salida+=parcial
			else:
				salida=salida+","+parcial
			i+=1

		salida+="]"
		return salida
		
		
api.add_namespace(ns1, path='/festivales')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8080)


