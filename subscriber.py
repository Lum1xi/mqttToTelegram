import paho.mqtt.client as mqtt
from config import TOPIC, BROKER, PORT
import queue

def get_message():
    q = queue.Queue()

    def on_message(client, userdata, message):
        q.put(message.payload.decode())
        client.disconnect()

    client = mqtt.Client()
    client.on_message = on_message

    client.connect(BROKER, PORT)
    client.subscribe(TOPIC)

    client.loop_start()
    msg = q.get()
    client.loop_stop()

    return msg
