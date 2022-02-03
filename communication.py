import os
import serial
from time import sleep
import numpy as np

sample_rate=3200
length_s = 5

def read_data():
	os.system(f'sudo adxl345spi -t {length_s} -f {sample_rate} -s out.csv')
	acc_data = np.genfromtxt('out.csv', delimiter=',', names=True)
	
	for i in range(len(acc_data['time'])):
		ser.write(str(acc_data['time'][i]).encode('ascii'))
		ser.write(str(acc_data['z'][i]).encode('ascii'))
	
	ser.write('f'.encode('ascii'))
	
ser = serial.Serial('/dev/ttyS0', 9600)
while True:
	recieved_data = ser.read().decode()
	if recieved_data == 'r':
		read_data()
