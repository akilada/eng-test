from flask_restful import Resource
import logging as logger

class FlaskAPI(Resource):

    def get(self):

        logger.debug("Inside the post method of Task")

        projectDetails = {
                "version" : "1.0.0.0",
                "service_name" : "flaskAPI",
                "environment": {
                    "service_port": "8080",
                    "log_level": "INFO"
                }
        }


        return projectDetails,200