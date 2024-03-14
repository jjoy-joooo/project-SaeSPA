# Python 3.8 슬림 버전을 기반 이미지로 사용
FROM python:3.8-slim

# /app 디렉토리를 작업 디렉토리로 설정
WORKDIR /app

# 현재 디렉토리의 모든 파일을 컨테이너의 /app으로 복사
COPY . /app

# requirements.txt에 명시된 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# Gunicorn을 사용하여 Flask 앱 실행, 4개의 워커로 설정
CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:5000", "wsgi:app"]
