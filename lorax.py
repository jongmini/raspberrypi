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

def getserial():
  cpuserial= "0000000000000000"
  try:
    f = open('/proc/cpuinfo', 'r')
    for line in f:
      if line[0:6]=='Serial':
        cpuserial=line[10:26]
    f.close()
  except:
    cpuserial= "ERROR000000000"
  return cpuserial



while True:
  soil0 = ReadChannel(0)
  serial_id = getserial()
  if serial_id == "ERROR000000000":
    print "error"
  h = Http()		
  resp, content = h.request("http://murmuring-crag-3099.herokuapp.com/"+str(soil0)+"/"+serial_id+"/0", "POST")
  resp
  print resp
  time.sleep(10)



