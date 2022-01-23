import serial
import serial.tools.list_ports
import pyautogui
import time

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

placeholder,check = "",0
newdata = []
time.sleep(5)   # Delays for 5 seconds. You can also use a float value.

while True:
    data = arduino.readline() #Read the data received from the arduino
    newdata = data.split(" ") #sorts data in ascending order, and splits each keypress into a list
    del newdata[-1]
    if newdata[0] == "":
        del newdata[0]
    if newdata != "" or newdata != None:
        if newdata[0] == "\xff0":
            newdata[0] = '0'
        newdata = [int(x) for x in newdata]
    newerdata = ""
    if data == "" and placeholder is not "": 
        pyautogui.keyUp(placeholder) #keyup if no input detected + if placeholder has a previous input
        print("up: " + placeholder)
    else:
      for i in range(len(newdata)):
        newdata[i] = int(newdata[i]) #converts every value into int
        newerdata += (selectedKeys[newdata[i]]) #converts into keypress + appends into a string
      for i in range(len(newerdata)):
        if newerdata[i] not in selectedKeys: #check each value if it is the same as placeholder, check = 1 if different
          check = 1
      if check == 1: #if input is changed
        pyautogui.keyUp(placeholder)
        print("up: " + placeholder)
        pyautogui.keyDown(newerdata)
        print("down: " + newerdata)
        placeholder = newerdata
'''
while True:  #### LOGIC TO BE TESTED
    data = arduino.readline() #Read the data received from the arduino
    if data == '':
        pyautogui.keyUp(pressedKey)
        pressedKey = ''
    else:
        if data in selectedKeys:
            if data != pressedKey:
                placeholder = data.split(" ")
                pyautogui.keyUp(pressedKey)
                pressedKey = data
            pyautogui.keyDown(pressedKey)
    print(data)
'''