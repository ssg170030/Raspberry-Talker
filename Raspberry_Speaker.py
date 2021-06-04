import json
# import boto3
# import pygame
import paho.mqtt.client as mqtt
import pyttsx3


def say(robot):
    talk.say(robot)
    talk.runAndWait()


def dragon_connect(dragon_client, userdata, flags, rc):
    say("I am connect to Mqtt Online")
    print("MQtt is online")
    client.subscribe("sean/#")
    client.publish("dylan", "Hello")


def dragon_disconnect(client, userdata, rc):
    print("Disconnected from MQtt")
    say("HELP! I am disconnected")


def dragon_message(client, userdata, message):
    msg = message.payload.decode("utf-8").lower()
    print("message received:", msg)
    print("message topic:", message.topic)
    say(msg)
    if msg == 'hello':
        client.publish("dylan", "How are you")
        print("i got hello")
    elif msg == 'good':
        client.publish("dylan", "Good")

    elif msg == 'goodbye':
        client.publish("dylan", "See yah later.")

    elif msg == 'how are you?':
        client.publish("dylan", "fine, and you?")
        print("I got how are you.")


talk = pyttsx3.init()
say("Ready to work")

broker = "192.168.86.42"
broker_port = 1883
client = mqtt.Client("bleh", 60)
client.on_message = dragon_message

client.on_disconnect = dragon_disconnect
client.on_connect = dragon_connect
client.connect(broker, broker_port, keepalive=10)
