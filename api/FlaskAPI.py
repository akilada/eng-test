from flask_restful import Resource
from app import port, level, commit_sha, version
import logging as logger
import subprocess
import os

class FlaskAPI(Resource):

    def get(self):
 
        logger.debug("Inside the post method of Task")

        projectDetails = {
                "version" : "{0}".format(version),
                "git_commit_sha": "{0}".format(commit_sha),
                "service_name" : "flaskAPI",
                "environment": {
                    "service_port": "{0}".format(port),
                    "log_level": "{0}".format(level)
                }
        }

        return projectDetails,200