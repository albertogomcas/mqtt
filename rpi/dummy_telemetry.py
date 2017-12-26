import paho.mqtt.client as mqtt
import time
import random

client = mqtt.Client(protocol=mqtt.MQTTv31)

print(client.connect("10.0.0.10", 1883))

while True:
    print(client.publish('home/dummyfloor/dummyroom/temperature', str(random.random())))
    print(client.publish('home/dummyfloor/dummyroom/humidity', str(random.random())))
    print(client.publish('home/dummyfloor2/dummyroom2/temperature', str(random.random())))
    print(client.publish('home/dummyfloor2/dummyroom2/humidity', str(random.random())))
    print("pub")
    time.sleep(3)
