

docker build -t flaskapi --build-arg PORT=8080 --build-arg LOG_LEVEL=DEBUG --build-arg DEBUG=True  --build-arg VERSION=$(git describe --tags) --build-arg COMMIT=$(git log -1 --format=%h) .
 
docker run -it -d -p 8080:8080 flaskapi

docker exec -it <cointainer_id> bash