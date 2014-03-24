# this code reads the soil moisture level and prints the result every 5 seconds

import spidev
import time
import os

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

  time.sleep(5)