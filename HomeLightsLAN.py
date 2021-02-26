#!/usr/bin/python

from phue import Bridge
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import pdb;
b = Bridge('192.168.1.142')

#print(b.connect())

#print(b.get_api())

lights = b.lights

while(1):
    lightsCurrentStatus = -1
    time.sleep(1)
    response = urlopen('https://www.cyertai.com/lights/status')
    lightsCurrentStatus = response.read().decode('UTF-8')
    breakpoint()

    for light in lights:
        if (lightsCurrentStatus == "1"):
            if(light.on == False):
                light.on = True
                light.transiiontime = 1
                light.brightness = 254
        if (lightsCurrentStatus == "0"):
            if(light.on == True):
                light.on = False
        if (lightsCurrentStatus == "-1"):
            pass


