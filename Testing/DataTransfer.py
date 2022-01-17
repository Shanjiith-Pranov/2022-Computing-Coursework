import serial

arduino = serial.Serial('/dev/cu.usbmodem141101', 115200, timeout=.1)

while True:data = arduino.read();print(data)