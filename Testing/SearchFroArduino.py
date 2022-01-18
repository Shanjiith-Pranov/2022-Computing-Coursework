import serial
import serial.tools.list_ports

# IOUSBHostDevice is the arduino's tag or something, the serial value changes for each mac

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'IOUSBHostDevice' in p.description 
]
if not arduino_ports:
    print("No Arduino found")
if len(arduino_ports) > 1:
    print('Multiple Arduinos found - using the first')

ser = serial.Serial(arduino_ports[0])

##  /dev/cu.usbmodem141101 - IOUSBHostDevice

