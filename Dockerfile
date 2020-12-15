FROM registry.access.redhat.com/ubi8/python-38

LABEL name="FlaskAPI"
LABEL description="A simple API absed on python flask"
LABEL maintainer="Akila Amarathunga"

ARG WORK_DIR=/app

ARG PORT
ARG LOG_LEVEL
ARG DEBUG
ARG VERSION
ARG COMMIT

ENV flaskPort=$PORT
ENV flaskLogLevel=$LOG_LEVEL
ENV flaskDebug=$DEBUG
ENV version=$VERSION
ENV commit_sha=$COMMIT

USER root

RUN mkdir ${WORK_DIR}

WORKDIR ${WORK_DIR}

COPY . ${WORK_DIR}

RUN pip3 --no-cache-dir install -r requirements.txt && \
    chown -R 1001:1001 ${WORK_DIR} 

EXPOSE 8080

USER 1001

ENTRYPOINT ["python3"]
CMD ["app.py"]