FROM python:3.8

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:5000", "wsgi:app"]
