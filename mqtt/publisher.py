# PUBLISHER
import random

import paho.mqtt.client as mqtt
import json
import datetime
import random

random.seed()

client = mqtt.Client("Parrot")
client.connect("localhost")

datetime_object = datetime.datetime.now()

data = {
    "datetime": datetime_object.strftime("%F %T.%f"),
    "location": (23.5, 34.6),
    "readings": {
        "temperature": 32.4 - random.uniform(-10.0, 10.0),
        "humidity": 12.6,
    }
}

json_data = json.dumps(data)

client.publish("superheroes", json_data)
client.publish("superheroes/weather", json_data)
