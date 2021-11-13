# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 13:49:52 2020

@author: makn0023
"""

import paho.mqtt.client as mqtt
from datetime import datetime
import time
import json
from random import randint

inf = {"app_id":"hajo66","dev_id":"node1","port/channel":randint(0, 100),
       "rssi":randint(0, 100),"snr":randint(0, 100),
       "sf":"SF7BW125","C_F":"C","temperature":randint(0, 100),
       "time": datetime.now().strftime("%d-%b-%Y %H:%M:%S"),
       "messgae id/counter":randint(0, 100)}