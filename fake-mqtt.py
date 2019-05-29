#!/usr/bin/python
try:
  from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0
import random, time
import paho.mqtt.client as mqtt

mqtthost=''
mqttc = mqtt.Client()
mqttc.connect (mqtthost, "1883", 60)

while True:
  config = ConfigParser()
  config.read('fake.cfg')


  for section in config.sections():
    path=section
    type=str(config.get(section,"type"))
    min=int(config.get(section,"min"))
    max=int(config.get(section,"max"))
    value = random.randint(min,max)
    path=path + '/' + str(type)
    mqttc.publish(path,value)
  time.sleep(10)
