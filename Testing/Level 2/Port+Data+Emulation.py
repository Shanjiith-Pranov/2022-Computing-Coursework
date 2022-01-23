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

placeholder = newdata = ""
while True:
    newdata = ""
    data = (arduino.readline()).split(" ") #Read the data receiveda from the arduino
    del data[-1]
    for i in range(len(data)):
        data[i] = int(data[i]) #converts every value into int
        newdata = newdata + selectedKeys[data[i]] #converts into keypress + appends into a string
    if placeholder != newdata:
        pyautogui.keyUp(placeholder) #keyup if no input detected + if placeholder has a previous input
        print("up: " + placeholder + "\n")
        pyautogui.keyDown(newdata) #keyup ssdddddif no input detected + if placeholder has a previous input
        print("down: " + newdata + "\n")
        placeholder = newdata

'''dadd
placeholder = ""
newdata = []
time.sleep(5)   # Delays for 5 seconds. You can also use a float value.

while True:
    check = check0 = 0
    data = arduino.readline() #Read the data received from the arduino
    #print(data)

    newdata = data.split(" ") #sorts data in ascending order, and splits each keypress into a list
    del newdata[-1]
    if newdata == [] or newdata == None:
        print("nothing sent")
        check0 = 1
    else: 
        # newdata != [] or newdata != None:
        if newdata[0] == "\xff0" or newdata[0] == "\xfc0":
            newdata[0] = ''
        #newdata = [int(x) for x in newdata]
    newerdata = ""
    if check0 == 1 and placeholder is not "": 
        pyautogui.keyUp(placeholder) #keyup if no input detected + if placeholder has a previous input
        print("up: " + placeholder)
    else:
      for i in range(len(newdata)):
        newdata[i] = int(newdata[i]) #converts every value into int
        newerdata = newerdata + selectedKeys[newdata[i]] #converts into keypress + appends into a string

      for i in range(len(newerdata)):
        if newerdata[i] not in selectedKeys: #check each value if it is the same as placeholder, check = 1 if different
          check = 1

      if check == 1: #if input is changed
        pyautogui.keyUp(placeholder)
        print("up: " + placeholder)
        pyautogui.keyDown(newerdata)
        print("down: " + newerdata)
    placeholder = newerdata

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