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


def loadUI(): #Shanjiith
    import UI

def searchArduino(): #Shanjiith + Darius + Hern Yee
    global arduino
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
            arduino = Serial(arduino_ports[0], 115200, timeout=.1) # Set the serial of the arduino of serial coomunication
            break #Break out of the loop once the arduino is found 

def SendEnable(): #Hern Yee/Returns enabledKeys
    return enabledKeys

def Search(): #Shanjiith/ Searches for arduino
    try:
        searchArduino()
    except Exception as exception:
        data = open("arduino.txt",'w')
        data.write("0")
        data.close()
        arduino[0] = False

def StartStop(): #Shanjiith + Darius
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

def emulator(): #Shanjiith + Hern Yee + Darius
    global selectedKeys,enabledKeys,placeholder,newdata,arduino
    arduinoValue = open("arduino.txt", "r") #opening arduino.txt to fetch state
    if int(arduinoValue.readline())  == 1:
        arduinoValue.close()
        toggle = open("toggle.txt", "r") #opening arduino.txt to fetch state
        # while True:
        if  toggle.readline()  == '1':
            
            keys = open("keys.txt", "r") #opening arduino.txt to fetch state
            selectedKeys = keys.readline().split() #fetching data from arduino.txt
            keys.close()
            newdata=[]
            pressedKeys = (arduino.readline()).decode().split(" ") #Read the data received from the arduino
            enabledKeys = (arduino.readline()).decode().split(" ") #Read the data received from the arduino
            del pressedKeys[-1]
            if len(pressedKeys)>0:
                if len(pressedKeys[0]) != 1:
                    pressedKeys[0] = pressedKeys[0][-1]
            for i in range(len(pressedKeys)):
                pressedKeys[i] = int(pressedKeys[i]) #converts every value into int
                newdata.append(selectedKeys[pressedKeys[i]]) #converts into keypress + appends into a string
            if placeholder != newdata:
                for j in placeholder:
                    if j in newdata:
                        pass
                    else:
                        if j == "macro_1":
                            macro = open("macros.txt", "r") #opening arduino.txt to fetch state
                            keyUp(macro.readline()) #fetching data from arduino.txt
                            macro.close()
                        elif j == "macro_2":
                            macro = open("macros.txt", "r") #opening arduino.txt to fetch state
                            _ = macro.readline()
                            keyUp(macro.readline()) #fetching data from arduino.txt
                            macro.close()
                        else:
                            keyUp(j) #keyup if no input detected + if placeholder has a previous input
                for k in newdata:
                    if k in placeholder:
                        pass
                    else:
                        if k == "macro_1":
                            macro = open("macros.txt", "r") #opening arduino.txt to fetch state
                            macroText = macro.readline()
                            for l in macroText:
                                keyDown(l) #fetching data from arduino.txt
                            macro.close()
                        elif k == "macro_2":
                            macro = open("macros.txt", "r") #opening arduino.txt to fetch state
                            _ = macro.readline()
                            macroText = macro.readline()
                            for l in macroText:
                                keyDown(l) #fetching data from arduino.txt
                            macro.close()
                        else:
                            keyDown(k) #keyup ssdddddif no input detected + if placeholder has a previous input
                placeholder = newdata
        else:
            toggle.close()
            # break
    else:
        pass

loadUI()