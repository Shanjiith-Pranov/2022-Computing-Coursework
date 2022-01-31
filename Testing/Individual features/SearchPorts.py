import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports()) #Find all the connected ports
for p in ports:
    print(p) # Print all the ports