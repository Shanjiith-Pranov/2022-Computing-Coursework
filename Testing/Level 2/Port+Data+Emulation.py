import serial
import serial.tools.list_ports
import pyautogui

keys = ['a', 'b', 'c', 'd'] # make this a changable variable later on when the mapping function is added
pressedKey = ''

while True:
    arduino_ports = [ # Find all the ports with "IOUSBHostDevice" as its tag
        p.device
        for p in serial.tools.list_ports.comports()
        if 'IOUSBHostDevice' in p.description   # IOUSBHostDevice is the arduino's tag or something, the serial value changes for each mac so we cannot search using that
    ]
    if not arduino_ports: #Loops until arduino is found
        continue
    if len(arduino_ports) > 1:
        print('Multiple Arduinos found - using the first')

    print("Arduino found") # Arduino is found
    arduino = serial.Serial(arduino_ports[0]) #initialize connection with arduino
    break #Break out of the loop once the arduino is found

while True:  #### LOGIC TO BE TESTED
    data = arduino.read() #Read the data received from the arduino
    if data == '':
        pyautogui.keyUp(pressedKey)
        pressedKey = ''
    else:
        if data in keys:
            if data != pressedKey:
                pyautogui.keyUp(pressedKey)
                pressedKey = data
            pyautogui.keyDown(pressedKey)
