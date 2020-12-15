from flask import Flask
import logging as logger
logger.basicConfig(level="INFO")


flaskAppInstance = Flask(__name__)


if __name__ == '__main__':

    logger.debug("Starting FlaskAPI Server")
    from api import *
    flaskAppInstance.run(host="0.0.0.0",port=8080,debug=False,use_reloader=True)