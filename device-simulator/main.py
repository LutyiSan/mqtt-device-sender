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
        

    def create_client(self):
        self.client.ws_set_options(path=self.url_path, headers=None)
        self.client.username_pw_set(self.user_name, password=self.user_pass)
        logger.debug(f"{self.url_path} client created READY")
        # Если требуется ssl (wss)
        # client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=None,tls_version=ssl.PROTOCOL_TLS, ciphers=None)
        # client.tls_insecure_set(True)

    def lift(self):
        device = {"name": "lift", "stage11": False, "stage12": False, "stage13": False, "stage14": False,
                "stage15": False, "stage16": False, "stage17": False,"stage21": False, "stage22": False, "stage23": False, "stage24": False,
                "stage25": False, "stage26": False, "stage27": False, "door": False, "door2" :False, "door3": False, "stage31": False, "stage32": False, "stage33": False, "stage34": False,
                "stage35": False, "stage36": False, "stage37": False,}
        stage1 = random.choice([11,12,13,14,15,16,17])
        door1 = random.choice([True, False, False, True, True, False])
        stage2 = random.choice([21,22,23,24,25,26,27])
        door2 = random.choice([True, False, False, True, True, False])
        stage3 = random.choice([31,32,33,34,35,36,37])
        door3 = random.choice([True, False, False, True, True, False])
        for i in device.keys():
            #print(i)
            if str(stage1) in i:
              #  print(str(stage))
              #  print (i)
                device[i] = True
                device["door"] = door1
  
            if str(stage2) in i:
              #  print(str(stage))
              #  print (i)
                device[i] = True
                device["door2"] = door2
        
     
            if str(stage3) in i:
              #  print(str(stage))
              #  print (i)
                device[i] = True
                device["door3"] = door3           
        self.send_json = json.dumps(device)
        self.client.publish(f"lucenko/{device['name']}", payload=self.send_json, qos=0, retain=True)
        logger.debug(f"Publish topic lucenko/{device['name']}...")
        
    def scud(self):
        device = {"name": "scud", "td1": False, "td1alarm": False, "td2": False, "td2alarm": False,
                "td3": False, "alarm": False, "td4": False, "td4alarm": False}
        td = random.choice([1,2,3,4])
        #door = random.choice([True, False, False, True, True, False])
        for i in device.keys():
            #print(i)
            if str(td) in i:
                #print(str(td))
                #print (i)
                device[f'td{td}'] = True
                alarm = random.choice([False, False, False, False,True,False,False, False, False,True])
                device[f'td{td}alarm'] = alarm
                break
                
                


        self.send_json = json.dumps(device)
        self.client.publish(f"lucenko/{device['name']}", payload=self.send_json, qos=0, retain=True)
        logger.debug(f"Publish topic lucenko/{device['name']}...")

    def connect_client(self):
        self.client.connect(self.broker, port=self.broker_port, keepalive=60, bind_address="")
        logger.debug(f"Connection to {self.broker}:{self.broker_port} READY")

    def publishing(self):
        devices = DEVICES
        for device in devices:
            if device['name'] == "lift":
                self.lift()
            elif device['name'] == "scud":
                self.scud()
            else:
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
