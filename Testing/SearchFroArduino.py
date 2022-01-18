import serial
import serial.tools.list_ports
import time

# IOUSBHostDevice is the arduino's tag or something, the serial value changes for each mac
while True:
    arduino_ports = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'IOUSBHostDevice' in p.description 
    ]
    if not arduino_ports:
        print("No Arduino found")
        continue
    if len(arduino_ports) > 1:
        print('Multiple Arduinos found - using the first')

    ser = serial.Serial(arduino_ports[0])
    print("Arduino found")
    break

    ##  /dev/cu.usbmodem141101 - IOUSBHostDevice

