import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports()) #Find all the connected ports
for p in ports:
    print(p) # Print all the ports

'''
import serial
import serial.tools.list_ports

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'IOUSBHostDevice' in p.description  # may need tweaking to match new arduinos
]
if not arduino_ports:
    print("No Arduino found")
if len(arduino_ports) > 1:
    print('Multiple Arduinos found - using the first')

ser = serial.Serial(arduino_ports[0])

##  /dev/cu.usbmodem141101 - IOUSBHostDevice
'''