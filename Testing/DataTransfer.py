#Python code for connecting Arduino to Python
#That's Engineering
#29/04/2020

import serial
import time


def main_func():
    arduino = serial.Serial('/dev/cu.usbmodem141101', 9600) #Established serial connection to Arduino
    arduino_data = arduino.read()
    arduino_data2 = arduino.read()
    print(arduino_data)
    print(arduino_data2)

    #arduino.close()#Connection closed
    


# ----------------------------------------Main Code------------------------------------
# Declare variables to be used


print('Program started')


while True:
    main_func()