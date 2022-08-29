import adafruit_dht
import board
import time

sensor = adafruit_dht.DHT11(board.D18)

while True:
    try:
        temp = sensor.temperature
        humi = sensor.humidity
        print("{:.2f} °C, {:.2f} %".format(temp, humi))

    except RuntimeError as e:
        print("Oops, reading the sensor did not work.")

    time.sleep(5)
