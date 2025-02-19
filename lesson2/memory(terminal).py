import serial
import time

ser = serial.Serial('COM9', timeout=1)
time.sleep(1)

while True:
    text = 'Hello, world'
    ser.write((text).encode('utf-8'))
    print(ser.read(15).decode('utf-8'))
    time.sleep(1)
