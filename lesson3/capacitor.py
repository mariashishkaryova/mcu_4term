import serial
import time

ser = serial.Serial('COM9', timeout=1)
time.sleep(0.5)

start_time = time.time()

while time.time() - start_time < 60:

    ser.write(('1').encode('utf-8'))
    data = ser.read(20).decode('utf-8')
    time.sleep(0.5)

    f = open('capacitor.txt', 'a')
    f.write(data)
    print(data)