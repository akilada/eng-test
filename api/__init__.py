
from flask_restful import Api
from app import flaskAppInstance
from .FlaskAPI import FlaskAPI



restServerInstance = Api(flaskAppInstance)

restServerInstance.add_resource(FlaskAPI,"/info")