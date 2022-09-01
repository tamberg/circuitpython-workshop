from random import randint
import ssl
import time
import wifi
import socketpool
import adafruit_minimqtt.adafruit_minimqtt as minimqtt

WIFI_SSID = "MY_SSID" # TODO
WIFI_PASS = "MY_PASSWORD" # TODO

# See https://ch.mathworks.com/help/thingspeak/mqtt-basics.html
MQTT_HOST = "mqtt3.thingspeak.com"
MQTT_PORT = 8883

# https://thingspeak.com/devices/mqtt > Add a device
MQTT_CLNT = "***********************" # TODO, Client ID
MQTT_USER = "***********************" # TODO, Username
MQTT_PASS = "***********************" # TODO, Password
THSP_CHAN = "000000" # TODO, ThingSpeak Channel ID

print("Connecting to Wi-Fi \"{0}\"...".format(WIFI_SSID))
wifi.radio.connect(WIFI_SSID, WIFI_PASS) # waits for IP address
print("Connected, IP address = {0}".format(wifi.radio.ipv4_address))

pool = socketpool.SocketPool(wifi.radio)
context = ssl.create_default_context()

def handle_connect(client, userdata, flags, rc):
    print("Connected to {0}".format(client.broker))

def handle_publish(client, userdata, topic, pid):
    print("Published to {0} with PID {1}".format(topic, pid))

mqtt_client = minimqtt.MQTT(
    broker = MQTT_HOST,
    port = MQTT_PORT,
    client_id = MQTT_CLNT,
    username = MQTT_USER,
    password = MQTT_PASS,
    socket_pool = pool,
    ssl_context = context)

mqtt_client.on_connect = handle_connect
mqtt_client.on_publish = handle_publish

print("\nConnecting to {0}...".format(MQTT_HOST))
mqtt_client.connect()

while True:
    value = 23 # e.g. from sensor
    mqtt_topic = "channels/" + THSP_CHAN + "/publish"
    mqtt_payload = "field1=" + str(value)
    mqtt_client.publish(mqtt_topic, mqtt_payload)
    time.sleep(5)
