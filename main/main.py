from serial import Serial
from serial.tools.list_ports import comports
from pyautogui import keyDown
from pyautogui import keyUp
from time import time

selectedKeys = ["w","a","s","d","esc"] # the keys that are currently selected, cuztomisable list
enabledKeys = []

placeholder =''
newdata = []
arduino = [False,None]
startstop = 0

def searchArduino():
    t_end = time() + 9
    while time() < t_end:
        arduino_ports = [ # Find all the ports with "IOUSBHostDevice" as its tag
            p.device
            for p in comports()
            if 'IOUSBHostDevice' in p.description   # IOUSBHostDevice is the arduino's tag or something, the serial value changes for each mac so we cannot search using that
        ]
        if not arduino_ports: #Loops until arduino is found
            data = open("arduino.txt",'w')
            data.write("0")
            data.close()
            continue
        else:
            data = open("arduino.txt",'w')
            data.write("1")
            data.close()
            if len(arduino_ports) > 1:
                arduino = [True, Serial(arduino_ports[0], 115200, timeout=.1)] #initialize connection with arduino
            break #Break out of the loop once the arduino is found 



def SendEnable():
    return enabledKeys

def Search():
    try:
        searchArduino()
    except Exception as exception:
        data = open("arduino.txt",'w')
        data.write("0")
        data.close()
        arduino[0] = False

def StartStop():
    toggle = open("toggle.txt", "w")
    global startstop
    if startstop == 1:
        startstop = 0
        toggle.write("0") #fetching data from arduino.txt
        emulator()
    elif startstop == 0:
        startstop = 1
        toggle.write("1") #fetching data from arduino.txt
        emulator()
    else:
        startstop = 0
    toggle.close()    

import UI

def emulator():
    global selectedKeys,enabledKeys,placeholder,newdata,arduino
    if arduino[0]:
        f = open("test.txt",'w')
        f.write("running")
        f.close()
        toggle = open("toggle.txt", "r") #opening arduino.txt to fetch state
        while True:
            if  int(toggle.readline())  == 1:
                arduino = open("keys.txt", "r") #opening arduino.txt to fetch state
                selectedKeys = arduino.readline().split() #fetching data from arduino.txt
                arduino.close()
                newdata=[]
                pressedKeys = (arduino[1].readline()).split(" ") #Read the data received from the arduino
                enabledKeys = (arduino[1].readline()).split(" ") #Read the data received from the arduino
                del pressedKeys[-1]
                if pressedKeys[0] == "\xff0":
                    pressedKeys[0] = '0'
                for i in range(len(pressedKeys)):
                    pressedKeys[i] = int(pressedKeys[i]) #converts every value into int
                    newdata.append(selectedKeys[pressedKeys[i]]) #converts into keypress + appends into a string
                if placeholder != newdata:
                    print(newdata)
                    for j in placeholder:
                        if j in newdata:
                            pass
                        else:
                            keyUp(j) #keyup if no input detected + if placeholder has a previous input
                    for k in newdata:
                        if k in placeholder:
                            pass
                        else:
                            if pressedKeys[newdata]:
                                keyDown(k) #keyup ssdddddif no input detected + if placeholder has a previous input
                    placeholder = newdata
            else:
                toggle.close()
                break
    else:
        pass