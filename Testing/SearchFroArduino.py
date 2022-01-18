import serial
import serial.tools.list_ports
import time

while True:
    arduino_ports = [ # Find all the ports with "IOUSBHostDevice" as its tag
        p.device
        for p in serial.tools.list_ports.comports()
        if 'IOUSBHostDevice' in p.description   # IOUSBHostDevice is the arduino's tag or something, the serial value changes for each mac
    ]
    if not arduino_ports: #Loops until arduino is found
        continue
    if len(arduino_ports) > 1:
        print('Multiple Arduinos found - using the first')

    print("Arduino found") # Arduino is found
    ser = serial.Serial(arduino_ports[0]) # Set the serial of the arduino of serial coomunication
    
    break #Break our of the loop once the arduino is found



