FROM python:3.8-slim
WORKDIR /usr/src/app
COPY readscript.py ./
RUN pip install Adafruit_DHT prometheus_client
CMD ["python", "./readscript.py"]
