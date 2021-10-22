FROM python:3.10-alpine

# WORKDIR: RUN, CMD, ENTRYPOINT의 명령이 실행될 디렉터리를 설정한다.
# WORKDIR <경로>
# 다음 명령들은 /usr/src/app 디렉토리에서 실행된다.
WORKDIR /usr/src/app

# COPY: 파일을 이미지에 추가한다.
# COPY <복사할 파일 경로> <이미지에서 파일이 위치할 경로>
# requirements/dev.txt 파일을 /usr/src 디렉토리로 복사한다.
COPY requirements/dev.txt ./

# RUN: 셸 스크립트 구문을 실행한다.
# RUN <명령>
# RUN은 실행 결과를 캐시하여 다음 빌드 때 재사용한다. 재사용하지 않으려면 --no-cache 옵션을 사용한다.
RUN python3 -m ensurepip
RUN pip install -r dev.txt

# ENV: 환경 변수를 설정한다.
# ENV <환경 변수> <값>
# docker run -e <환경 변수>=<값>으로 사용가능
ENV PYTHONPATH "${PYTHONPATH}:/usr/src"

# 셸 없이 바로 실행하기
# CMD ["<실행 파일>", "<매개 변수1>", "<매개 변수2>", ...]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]