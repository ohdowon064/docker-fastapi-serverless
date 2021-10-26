# docker-fastapi-serverless
FastAPI를 Docker Container로 개발하고 AWS Lambda를 이용하여 배포하는 튜토리얼입니다.

```
$ docker-compose build lambda-fastapi-prod
$ docker push <AWS ECR repository URI>
```

```
$ npm install -g serverless
$ npm install
```

```
$ serverless deploy --stage dev 
```
