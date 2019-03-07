from flask import request
import json
from pymongo import MongoClient
from flask_restplus import Namespace, Resource,fields,reqparse
from application.festivales.festivalesRest import api
from flask_cors import CORS, cross_origin


def normalizacion(cadena):
	cadena=cadena.replace("\"","").replace("'","").replace(": ","\":\"").replace(", ","\",\"").replace("{","{\"") \
				.replace("}","\"}")
	return cadena.replace("http\":\"","http:").replace("https\":\"","https:")

client = MongoClient('mongodb+srv://cluster0-lhfgs.gcp.mongodb.net/test',username='javig13' \
	,password='Estudiantes15',connect=False)

class consulta(Resource):
	@cross_origin()
	def get(self):
	return "hello"
	"""
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
	"""
