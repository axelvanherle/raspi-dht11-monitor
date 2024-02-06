import Adafruit_DHT
import time
from prometheus_client import start_http_server, Gauge

def read_sensor():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio_pin)
    print(temperature, humidity)
    temperature_gauge.set(temperature)
    humidity_gauge.set(humidity)

sensor = Adafruit_DHT.DHT11
gpio_pin = 4 # Change to what you're using
temperature_gauge = Gauge('room_temperature', 'Room temperature in celsius')
humidity_gauge = Gauge('room_humidity', 'Room humidity in percent')
start_http_server(8000)

while True:
    read_sensor()
    time.sleep(60) # read every 60 seconds
