# this code reads the soil moisture level and prints the result every 5 seconds
from httplib2 import Http
from urllib import urlencode
import spidev
import time
import os
#cpuinfo = open("/proc/cpuinfo","r")



spi = spidev.SpiDev()
spi.open(0,0)

def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3)<<8)+adc[2]
  print adc
  print data
  return data

while True:
  soil0 = ReadChannel(0)
  h = Http()		
  data = dict(reading=soil0,user_id=4,plant_id=3)
  resp, content = h.request("http://murmuring-crag-3099.herokuapp.com/4/3/"+str(soil0), "POST")
  resp
  print resp
  #print urlencode(data)
  time.sleep(10)



