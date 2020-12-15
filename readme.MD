
# A simple Python Flask API

## Purpose

The purpose of the project is to build a simple python flask based API endpoint.

## Assumptions

* Virtualbox installed on the developer's workstation
* Virtualbox used as the vmdriver for minikube 

## pre-requisites

- [![Minikube](https://img.shields.io/badge/Minikube-v1.15.1-brightgreen)](https://kubernetes.io/docs/setup/minikube/)
- [![Docker](https://img.shields.io/badge/Docker-19.03.13-brightgreen)](https://www.docker.com)
- [![Kubernetes](https://img.shields.io/badge/Kubbernetes-v1.20-brightgreen)](https://kubernetes.io/)
- [![Python](https://img.shields.io/badge/Python-3.8-brightgreen)](https://www.python.org/downloads/release/python-380/)

## Flask API Endpoints

The following are API enpoints avenabling one to:

* Request project details

## List of functioning Endpoints

| EndPoint      | Functionality | Actual Route  |
| ------------- |:-------------:| -----:|
| GET /info     | Endpoint returns project details in JSON format | /info |

## Build and Run

### Docker Build

```bash

        // build a docker image
        docker build -t <imageName:version> \
           --build-arg PORT=8080 
           --build-arg LOG_LEVEL=DEBUG 
           --build-arg DEBUG=True  
           --build-arg VERSION=$(git describe --tags)
           --build-arg COMMIT=$(git log -1 --format=%h) .

        
        // The following commnds can be used to test the image locally
        docker run -it -d -p <outsidePort>:<dockerInsidePort> <imageName:version>

        curl http://localhost:<outsidePort>/info
```

### Docker tag and push

```bash
        // Tag the docker image
        docker tag <imageName:version> <public_repository>/<imageName:version>

        
        // Push the docker image
        docker push <public_repository>/<imageName:version>
```
### Minikube Start

- Start minikube
```bash

    minikube start --memory=2048 --vm-driver=virtualbox --cpus=2 --kubernetes-version=v1.20.0

```

- Enable metrics on minikube
```bash

    minikube addons enable metrics-server

```

- Create a namespace
```bash

    kubectl create namespace <name>

```

- Deploy FlaskAPI temaplte 
```bash

    kuectl apply -f ./k8s-template.yml

```

- Set minikube IP
```bash

    export MINIKUBE_HOST=`minikube ip`

```

## Test

- Run curl command to test
```bash

    curl $MINIKUBE_HOST:30101/info

```

## Load Test

- Run following command to test HPA
```bash

    while true; do wget -q -O- curl $MINIKUBE_HOST:30101/info; done

```