# python3.6

import random

from paho.mqtt import client as mqtt_client



broker = '10.224.82.62'
# broker = 'localhost'
port = 9002

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id, transport='websockets')
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client, topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    topic1 = "mqtt/dashboard"
    subscribe(client, topic1)

    topic2 = "mqtt/top_vehicles"
    subscribe(client, topic2)
    client.loop_forever()


if __name__ == '__main__':
    run()