############################################################################################################
#  Это программа для имитации отправки сообщеий на mqtt-брокер устройствами по протоколу WS  в виде JSON   #
############################################################################################################
import random
import paho.mqtt.client as mqttc
import json
from random import uniform, randint
import time
from loguru import logger
from env import DEVICES, MQTT_PARAMS


class DeviceSimulator:

    def __init__(self):
        logger.add("/logs/mqtt_logs.log", format="{time: HH:mm:ss at DD-MM-YY} | {level} | {message}", rotation="2MB")
        self.publisher = MQTT_PARAMS['PUBLISHER']  # Client ID
        self.type = MQTT_PARAMS['TRANSPORT']  # tcp or websockets
        self.url_path = MQTT_PARAMS['PATH']  # /wss or /mqtt
        self.user_name = MQTT_PARAMS['USER_NAME']  # login
        self.user_pass = MQTT_PARAMS['USER_PASS']  # password
        self.broker = MQTT_PARAMS['HOST']  # mqtt broker url
        self.broker_port = MQTT_PARAMS['PORT']  # mqtt broker port
        self.sleeping_time = MQTT_PARAMS['SLEEPING_TIME']  # time between publishing in seconds
        self.client = mqttc.Client(client_id=self.publisher + str(randint(1234, 56789)), clean_session=True,
                                   userdata=None, protocol=mqttc.MQTTv311,
                                   transport=self.type)
        self.devices = DEVICES  # devices which is emulated here


    def create_client(self):
        self.client.ws_set_options(path=self.url_path, headers=None)
        self.client.username_pw_set(self.user_name, password=self.user_pass)
        logger.debug(f"{self.url_path} client created READY")
        # Если требуется ssl (wss)
        # client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=None,tls_version=ssl.PROTOCOL_TLS, ciphers=None)
        # client.tls_insecure_set(True)

    def connect_client(self):
        self.client.connect(self.broker, port=self.broker_port, keepalive=60, bind_address="")
        logger.debug(f"Connection to {self.broker}:{self.broker_port} READY")

    def publishing(self):
        for device in self.devices:
            for key, value in device.items():
                if key == 'name':
                    pass
                else:
                    if value == True or value == False:
                        curr_v = random.choice([True, False, True, False])

                        device[key] = curr_v
                    elif isinstance(value, (int, float)):
                        
                        curr_v = round(uniform(device[key] * 0.99, device[key] * 1.01), 2)
                        device[key] = curr_v

            self.send_json = json.dumps(device)
            self.client.publish(f"lucenko/{device['name']}", payload=self.send_json, qos=0, retain=True)
            logger.debug(f"Publish topic lucenko/{device['name']}...")


def run():
    ds = DeviceSimulator()
    ds.create_client()
    ds.connect_client()
    retry = 0
    while True:
        retry += 1
        ds.publishing()
        logger.debug(f'Publish count...... {retry}')
        time.sleep(ds.sleeping_time)


if __name__ == "__main__":
    logger.info('Start publishing')
    run()
