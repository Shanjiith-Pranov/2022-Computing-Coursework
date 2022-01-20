import serial
import serial.tools.list_ports
import pyautogui

keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","[","]","\\",";","'",",",".","/","up","down","left","right"] #The list of all possible keys
selectedKeys = ["w","a","s","d"] # the keys that are currently selected, cuztomisable list

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
    arduino = serial.Serial(arduino_ports[0], 115200, timeout=.1) #initialize connection with arduino
    break #Break out of the loop once the arduino is found

while True:  #### LOGIC TO BE TESTED
    data = arduino.readline() #Read the data received from the arduino
    if data == '':
        pyautogui.keyUp(pressedKey)
        pressedKey = ''
    else:
        if data in keys:
            if data != pressedKey:
                pyautogui.keyUp(pressedKey)
                pressedKey = data
            pyautogui.keyDown(pressedKey)
    print(data)