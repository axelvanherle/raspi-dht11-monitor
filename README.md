# raspi-dht11-monitor

![image](https://github.com/axelvanherle/raspi-dht11-monitor/assets/94362354/135d6798-e5e1-4877-8a7d-12622542ebe9)

Turn your raspberry pi into a monitoring device using a dht11 sensor.

*This project is known to work on a raspberry pi 3b+, your mileage may vary.*

This project uses a Raspberry Pi to read temperature and humidity data from a DHT11 sensor using python, and then publish these metrics to a Prometheus server. We use Grafana for data visualization, it gets the data from Prometheus. All this is done with docker compose, so you dont have to do shit but run it.

## How to
1) Install raspbian lite (64bit)
2) Install [docker](https://docs.docker.com/engine/install/debian/)
3) Clone this repo and change your working dir to it
4) Run `docker compose up -d`
5) Place it somewhere, and forget about it.

![image](https://github.com/axelvanherle/raspi-dht11-monitor/assets/94362354/528232a3-3cff-451b-a3bd-298495334c9f)
