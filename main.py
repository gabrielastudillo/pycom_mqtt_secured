#!/usr/bin/env python
#
# Copyright (c) 2019, Pycom Limited.

from network import WLAN
from mqtt import MQTTClient
import machine
import time
import socket
import ssl

def settimeout(duration): 
    pass

PARAMS = {'keyfile': 'cert/client.key', 
            'certfile': 'cert/client.csr', 
            'cert_reqs': ssl.CERT_REQUIRED, 
            'ca_certs': 'cert/client.crt'}

wlan = WLAN(mode=WLAN.STA)
#wlan.antenna(WLAN.EXT_ANT)
wlan.connect("XXXXXXXXX", auth=(WLAN.WPA2, "XXXXXXXXXX"), timeout=30000)

while not wlan.isconnected(): 
     machine.idle()

print("Connected to Wifi\n")
client = MQTTClient(' ', 'test.mosquitto.org', port=8884, keepalive=30, ssl=True, ssl_params = PARAMS)
client.settimeout = settimeout
client.connect()

while True:
     print("Sending ON")
     client.publish(topic="/lights", msg="ON")
     time.sleep(5)
     print("Sending OFF")
     client.publish(topic="/lights", msg="OFF")
     time.sleep(5)
