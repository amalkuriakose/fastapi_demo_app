# FastAPI Demo App

FastAPI is a Web framework for developing RESTful APIs in Python. This repo contains a FastAPI hello world app.

## Things I have learned

* Create a simple app using FastAPI
* Create docker image using Dockerfile

## Commands for creating, running and pushing ddocker image
```bash
  docker build -t amalkuriakose/fastapi-demo-app:v1.0.0 .

  docker run -p 8000:8000 amalkuriakose/fastapi-demo-app:v1.0.0

  docker push amalkuriakose/fastapi-demo-app:v1.0.0
 ```
