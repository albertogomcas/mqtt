import paho.mqtt.client as mqtt
import time

client = mqtt.Client(protocol=mqtt.MQTTv311)

client.connect("localhost", 1883)

while True:
    client.publish('home/dummy/val', str(time.time()))
    print("pub")
    time.sleep(3)
