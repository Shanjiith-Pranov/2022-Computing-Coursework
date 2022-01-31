import serial

arduino = serial.Serial('/dev/cu.usbmodem141101', 115200, timeout=.1) #initialize connection with arduino

while True:
    data = arduino.read() #Read the data received from the arduino
    print(data)