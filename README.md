## End to End MAchine Learning Project

## Run from terminal:
#### (Note: Don't forget '  **.**  ' at the first command and open Docker Destop app)

docker build -t testdockervearo.azurecr.io/mltest:latest .

docker login testdockervearo.azurecr.io

docker push testdockervearo.azurecr.io/mltest:latest
