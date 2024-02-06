FROM python:3.8-slim
WORKDIR /usr/src/app
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libgpiod2 build-essential
COPY readscript.py ./
RUN pip install Adafruit_DHT prometheus_client
CMD ["python", "./readscript.py"]
