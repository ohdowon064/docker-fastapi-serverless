FROM public.ecr.aws/lambda/python:3.8

# requirements/prod.txt파일을 LAMBDA_TASK_ROOT
# LAMBDA_TASK_ROOT는 AWS ECR에서 사용되는 루트 경로이다.
COPY requirements/prod.txt ${LAMBDA_TASK_ROOT}

# pip 설치 후에 requirements를 설치
RUN python3 -m ensurepip
RUN pip install -r prod.txt

# ADD는 파일을 이미지에 추가한다.
# ADD <복사할 파일 경로> <이미지에 파일이 위치할 경로>
# app 폴더를 LAMBDA_TASK_ROOT에 추가한다.
ADD app ${LAMBDA_TASK_ROOT}

# main.handler 파일을 실행한다.
CMD ["main.handler"]