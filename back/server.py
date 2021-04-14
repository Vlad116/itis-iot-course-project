import time
import json

import requests
from paho.mqtt import client as mqtt_client

broker = 'broker.hivemq.com'
port = 1883
topic1 = "vmk/team_6/r"
topic2 = "vmk/team_6/c"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-0'
worker_id = f'python-mqtt-1'
# username = 'emqx'
# password = 'public'

brokerT = 'thingsboard.cloud'
topicRequest1 = "tb/mqtt-integration-work/sensors/+/rx/twoway"
topicTelemetry = 'v1/devices/me/telemetry'
topicRequest = 'v1/devices/me/rpc/request/+'
topicResponse = 'v1/devices/me/rpc/response/'
# generate client ID with pub prefix randomly
# username = 'emqx'
# password = 'public'
ACCESS_TOKEN = 'Hj0payDBaIzqWowpoj0U'

publisher = mqtt_client.Client('5')
publisher.connect(broker, port)


def connect_mqtt(id, broker) -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
            print(broker)
            pass
        else:
            pass
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(id)
    if id == "0":
        # print("CONNECTED TO ", ACCESS_TOKEN)
        client.username_pw_set(ACCESS_TOKEN)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


light_publisher = connect_mqtt('0', brokerT)
light_publisher.loop_start()

sensors_per = []
data_list = []


def on_message(client, userdata, msg):
    from ast import literal_eval
    import json
    data = literal_eval(msg.payload.decode('utf8'))
    global sensors_per
    sensors_per = data
    print(sensors_per)
    data_list.append(sensors_per)
    # print('Incoming message topic: ' + msg.topic)

    # собственно если у нас сообщение начинается с sensor-1, мы посылаем ему сообщение (просто 10)
    if len(data) == 2:
        light_publisher.publish(topicTelemetry, json.dumps(sensors_per[0]))
    if msg.topic.startswith('tb/mqtt-integration-work/sensors/Sensor-1/rx/twoway'):
        # print('This is two way call, responding now')
        responseMsg = "{\"value\":\"200\"}"
        # print('Sending a response message: ' + responseMsg)
        publisher.publish("vmk/team_6/c", json.dumps(responseMsg))

        if len(sensors_per) == 2:
            client.publish(topicTelemetry, sensors_per[0])
            client.publish('v1/devices/me/rpc/response/1', sensors_per[0])
        # print('Sent a response message: ' + responseMsg)
        return
    # print(sensors_per)
    # print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")


def subscribe(client: mqtt_client):
    client.subscribe(topic1)
    # подписываемся на топик request
    client.subscribe(topicRequest1)
    client.subscribe(topicRequest)
    client.on_message = on_message


def publish(client):
    while True:
        if len(sensors_per) == 2:
            result = client.publish(topicTelemetry, json.dumps(sensors_per[0]))
            # print("PUBLISHING LIGHT: ", json.dumps(sensors_per[0]))
        time.sleep(30)


def run():
    import threading
    thread1 = threading.Thread(target=publish, args=[light_publisher])
    thread1.start()
    client = connect_mqtt('3', broker)
    subscribe(client)
    thread4 = threading.Thread(target=client.loop_forever)
    thread4.start()


def exec():
    run()


if __name__ == "__main__":
    exec()
    import pygame

    pygame.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    win = pygame.display.set_mode((500, 500))
    f1 = pygame.font.Font(None, 36)
    text = f1.render('Статус', True, (180, 0, 0))
    good = f1.render('Соответствие Госту', True, (180, 0, 0))
    average = f1.render('Средний уровень освещенности', True, (0, 0, 180))
    bad = f1.render('Место плохо освещено', True, (180, 0, 0))
    win.blit(text, (20, 0))
    is_send = False
    while True:
        if data_list:
            print(data_list)
            value = 300
            if not data_list[-1][-1].get('action'):
                value = data_list[-1][-1]['value']
            print(value)
            if value > 300:
                a = f1.render('Соответствие Госту', True, (0, 180, 0))
                is_send = False
            elif 80 < value < 300:
                a = f1.render('Средний уровень освещенности', True, (0, 0, 180))
                is_send = False
            else:
                a = f1.render('Место плохо освещено', True, (180, 0, 0))
                if not is_send:
                    is_send = True
            win.blit(a, (150, len(data_list) * 15))
        pygame.display.update()
