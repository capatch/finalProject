# Task 1, aurdino serial

import serial
import matplotlib.pyplot as plt

ser = serial.Serial('/dev/cu.usbmodem14401')
n=0
dataLst=[]
while n<200: # Collect 200 data points then stop
    print(ser.readline())
    dataPoint=ser.readline()
    dataPoint=int(dataPoint) # the data received are strings
    dataLst.append(dataPoint)
    n+=1
    
ser.close() # closes the serial port

plt.plot(dataLst) # plot the received data afterwards
plt.show
f=open('serialData.dat','w')
f.write(str(dataLst))
f.close()
f=open('serialData.dat','r')
print(f.read)
