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

## Shanjiith
def loadUI(): # Function to import and run the UI.py -> This import is a seperate function because importing and running UI.py and the begining causes a circular import and cross-file access does not work properly
    import UI

## Shanjiith + Darius + Hern Yee
def searchArduino(): 
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

## Shanjiith
def Search(): # Searches for arduino
    try:
        searchArduino()
    except Exception as exception: # Captures and exception error caused by the controller's arduino's port being using by another application
        data = open("arduino.txt",'w')
        data.write("0") # Changes the value in arduino.txt to "0" so the code recognises as no controller connected
        data.close()

## Shanjiith + Darius
def StartStop(): # Starts and stops the emulation
    toggle = open("toggle.txt", "w")
    global startstop
    if startstop == 1: # If the emulation is running
        startstop = 0
        toggle.write("0") # Change the value in toggle.txt to "0" so the code can read from the file and stop the emulation
        emulator()
    elif startstop == 0: # If the emulation is not running
        startstop = 1
        toggle.write("1") # Change the value in toggle.txt to "1" so the code can read from the file and start the emulation
        emulator()
    else:
        startstop = 0
    toggle.close()    

## Shanjiith + Hern Yee + Darius
def emulator():
    global selectedKeys,enabledKeys,placeholder,newdata,arduino
    arduinoValue = open("arduino.txt", "r") 
    if int(arduinoValue.readline())  == 1: # If the value in arduino.txt is '1' -> arduino is found
        arduinoValue.close()
        toggle = open("toggle.txt", "r") 
        if  toggle.readline()  == '1': # If the value in toggle.txt is '1' -> run emulation
            keys = open("keys.txt", "r") 
            selectedKeys = keys.readline().split() # Read the data in keys.txt and convert them into a list -> This value are the keys that the buttons will emulate 
            keys.close()
            newdata=[]
            pressedKeys = (arduino.readline()).decode().split(" ") # Read the data received from the arduino and split -> Example of recieved data: "0 3 4 /r/n"
            del pressedKeys[-1] # Remove the extra "/r/n"
            if len(pressedKeys)> 0:
                if len(pressedKeys[0]) != 1: # If the first value of the list is not a single digit, only get the last digit -> Some time when reading the data from the arduino, it add a random hex in front. This code is to remove that hex.
                    pressedKeys[0] = pressedKeys[0][-1]
            for i in range(len(pressedKeys)):
                pressedKeys[i] = int(pressedKeys[i]) # Converts every value into int
                newdata.append(selectedKeys[pressedKeys[i]]) # Converts into respective keys + appends into a string
            if placeholder != newdata: # If the placeholder, the keys that were previously pressed, is different from newdata -> Means that the keys pressed has changed.
                for j in placeholder:
                    if j in newdata:
                        pass # If the key is already pressed and there is an input to press it, there's no need to do anything
                    else:
                        if j == "macro_1" or j == "macro_2":
                            pass # If the key is a macro, don't do anything
                        else:
                            keyUp(j) # If the button is not pressed anymore, lift the key
                for k in newdata:
                    if k in placeholder:
                        pass # If the the key is already lifted and there is an input to lift it, there's no need to do it
                    else:
                        if k == "macro_1": 
                            macro = open("macros.txt", "r") 
                            macroText = macro.readline() 
                            macroText = macroText[:-2]
                            for l in macroText: # Press each key in the line and lift it after.
                                keyDown(l) 
                                keyUp(l) 
                            macro.close()
                        elif k == "macro_2":
                            macro = open("macros.txt", "r")
                            _ = macro.readline()
                            macroText = macro.readline() # Read the second line in the macros.txt
                            for l in macroText: # Press each key in the line and lift it after.
                                keyDown(l) 
                                keyUp(l)
                            macro.close()
                        else:
                            keyDown(k) # If the button is pressed, press the key
                placeholder = newdata # Save the current recieved data into placeholder -> Placeholder will be 1 loop behing the recieved data and is used to check the previously pressed keys
        else:
            toggle.close()
            # break
    else:
        pass

loadUI() # Load the UI