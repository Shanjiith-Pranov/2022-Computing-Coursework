import serial
import serial.tools.list_ports
import pyautogui
import time

keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","[","]","\\",";","'",",",".","/","up","down","left","right"] #The list of all possible keys
selectedKeys = ["w","a","s","d"] # the keys that are currently selected, cuztomisable list

pressedKey = ''
arduinoFound = False
placeholder = newdata = ""
arduino = None


def searchArduino(found,arduino):
    t_end = time.time() + 10
    while time.time() < t_end:
        arduino_ports = [ # Find all the ports with "IOUSBHostDevice" as its tag
            p.device
            for p in serial.tools.list_ports.comports()
            if 'IOUSBHostDevice' in p.description   # IOUSBHostDevice is the arduino's tag or something, the serial value changes for each mac so we cannot search using that
        ]
        if not arduino_ports: #Loops until arduino is found
            found = False
            continue
        else:        
            if len(arduino_ports) > 1:
                print('Multiple controllers found - using the first')
            else:
                print("Controller found") # Arduino is found
            found = True
            arduino = serial.Serial(arduino_ports[0], 115200, timeout=.1) #initialize connection with arduino
            break #Break out of the loop once the arduino is found 
    if not arduinoFound:
        print("Arduino not found")

def emulator(arduino):
    if arduinoFound:
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
    else:
        print('''Controller not found. 
        Common troubleshooting procedures:
        - Unplug the controller and plug it back in
        - Press the "Find controller" button
''')
    




while True:
    action = int(input("Enter selected action: "))
    if action == 0:
        searchArduino(arduinoFound,arduino)
    elif action == 1:
        emulator(arduino)
    else:
        break


