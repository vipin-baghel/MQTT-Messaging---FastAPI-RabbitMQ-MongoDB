import paho.mqtt.client as mqtt
import random
import time
import json


def on_publish(client, userdata, mid):
    print("Message Published with MID - ", mid)


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("mqtt_topic")


# def on_message(client, userdata, msg):
#     print(f"Received message: {msg.payload.decode()}")

# Create an MQTT client
client = mqtt.Client()

client.on_connect = on_connect
client.on_publish = on_publish
# client.on_message = on_message

client.username_pw_set(username="user", password="password")

client.connect("localhost", 1883, 60)

# Start the MQTT loop
client.loop_start()

# Publish messages to the MQTT topic every 1 second
while True:
    t = random.randint(0, 6)
    msg = {"status": t}
    client.publish("mqtt_topic", json.dumps(msg))
    time.sleep(1)
