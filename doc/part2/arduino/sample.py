#!/usr/bin/env python
import time
import numpy as np
import matplotlib.pyplot as plt
import serial

sr = serial.Serial('/dev/tty.usbmodem621',9600)

plt.axis([0, 1000, 0, 256])
plt.ion()
plt.show()

x,y = range(1, 1001),[]
while True:
  value = int(sr.readline())
  if len(y) >= 1000:
    y.pop(0) # to remove the first item
  y.append(value)
  plt.scatter(x[0:len(y)], y)
  plt.draw()
  time.sleep(0.05)
