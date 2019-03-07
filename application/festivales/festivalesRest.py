from flask_restplus import Namespace
api=Namespace("festivales/0.1","informacion de festivales")

from application.festivales.consultaFestivalesSpain import consulta
api.add_resource(consulta,'/consulta',endpoint="consulta festivales españoles")