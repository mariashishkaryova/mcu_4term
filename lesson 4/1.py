import serial
import time

ser = serial.Serial('COM9', timeout=1)
time.sleep(1)

start_time = time.time()

while time.time() - start_time < 40:

    ser.write(('1').encode('utf-8'))
    data = ser.read(25).decode('utf-8')
    time.sleep(0.1)

    f = open('bme.txt', 'a')
    f.write(data + '\n')
    print(data)