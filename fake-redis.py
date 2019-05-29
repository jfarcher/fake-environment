#!/usr/bin/python
try:
  from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0
import random, time
import redis

redishost=''
redisport=6379
redisdb=0
redistimeout=3
redthis=redis.StrictRedis(host=redishost,port=redisport, db=redisdb, socket_timeout=redistimeout)



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
    redthis.set(path,value)
  time.sleep(10)
