import serial
s = serial.Serial(port='/dev/tty.usbmodem1411', baudrate=9600)

while True:
    print int(float(s.readline()))