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

def loadUI():
    import UI

def searchArduino():
    t_end = time() + 5
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

def emulator(startstop):
    if startstop == 1:
        if arduino[0]:
            while True:
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
                    print("up: " + str(placeholder) + "\n")
                    for k in newdata:
                        if k in placeholder:
                            pass
                        else:
                            if pressedKeys[newdata]:
                                keyDown(k) #keyup ssdddddif no input detected + if placeholder has a previous input
                    print("down: " + str(newdata) + "\n")
                    placeholder = newdata
        else:
            pass
    else:
        pass

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
def StartStop(startstop):
    if startstop == 1:
        startstop = 0
    elif startstop == 0:
        startstop = 1
    else:
        startstop = 0
    emulator(startstop)
    

loadUI()
    