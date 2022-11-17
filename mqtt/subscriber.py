# SUBSCRIBER

# CTRL + ALT + L ==> Reformat code (CMD + OPT + L on Mac)
# CTRL + ALT + S ==> Settings (CMD + , on mac)

import paho.mqtt.client as mqtt
import json
from terminal_tricks.colours import Colours

# Define constant values
MQTT_SERVER = "localhost"
MQTT_CLIENT_NAME = "Duck"


def on_message_arrived(client, userdata, message):
    """
    Receives a message from the client.
    (Callback method)

    :param client:
    :param userdata:
    :param message: The message payload
    :return:
    """
    data = json.loads(message.payload.decode("utf-8"))
    datetime = data["datetime"]
    location = data["location"]
    temperature = data["readings"]["temperature"]
    humidity = data["readings"]["humidity"]
    topic = message.topic
    # | location | datetime | temperature | humidity | topic |
    print(f"|{Colours.bg.blue}{Colours.fg.pink}{(location)} "
          f"{Colours.reset}| {datetime} |"
          f" {temperature:5.2f} | {humidity:5.2f} | {topic:32} |")

    # print("message received ", str(message.payload.decode("utf-8")))
    # print("message topic=", message.topic)
    # print("message qos=", message.qos)
    # print("message retain flag=", message.retain)


def main():
    client = mqtt.Client()
    client.connect(MQTT_SERVER)
    client.subscribe("superheroes")
    client.subscribe("superheroes/weather")
    client.on_message = on_message_arrived
    client.loop_forever()


if __name__ == "__main__":
    main()
