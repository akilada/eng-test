from flask import Flask
import logging as logger
import os
import subprocess

#Environment variables
port       = int(os.environ.get("flaskPort", 8080))
level      = str(os.environ.get("flaskLogLevel", "INFO"))
debug      = str(os.environ.get("flaskDebug", "True"))
version    = os.environ.get("version")
commit_sha = os.environ.get("commit_sha")

# commit_sha = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD']).decode("utf-8").strip()
# version    = subprocess.check_output(['git', 'describe', '--tags']).strip().decode("utf-8").split("-")[0].strip()

logger.basicConfig(level=level)

flaskAppInstance = Flask(__name__)

if __name__ == '__main__':

    logger.debug("Starting FlaskAPI Server")
    from api import *
    flaskAppInstance.run(host="0.0.0.0",port=port,debug=debug,use_reloader=True)