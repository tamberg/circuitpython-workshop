import ssl
import time
import wifi
import socketpool

import adafruit_requests

WIFI_SSID = "MY_SSID" # TODO
WIFI_PASS = "MY_PASSWORD" # TODO
CLOUD_KEY = "..." # TODO, ThingSpeak Write API Key
CLOUD_URL = "https://api.thingspeak.com/update?api_key={0}".format(CLOUD_KEY)

print("Connecting to Wi-Fi \"{0}\"...".format(WIFI_SSID))
wifi.radio.connect(WIFI_SSID, WIFI_PASS) # waits for IP address
print("Connected, IP address = {0}".format(wifi.radio.ipv4_address))

socket = socketpool.SocketPool(wifi.radio)
context = ssl.create_default_context()
https = adafruit_requests.Session(socket, context)

while True:
    value = 23.0 # e.g. from sensor
    json_data = { "field1": value }
    print("{0}\n\n{1}".format(CLOUD_URL, json_data))
    response = https.post(CLOUD_URL, json=json_data)
    print(response.json())
    time.sleep(30) # s
