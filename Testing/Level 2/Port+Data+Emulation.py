import serial
import serial.tools.list_ports
import pyautogui
import time

keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","[","]","\\",";","'",",",".","/","up","down","left","right","esc"] #The list of all possible keys
selectedKeys = ["w","a","s","d","esc"] # the keys that are currently selected, cuztomisable list

placeholder =''
newdata = []
arduino = [False,None]


def searchArduino():
    t_end = time.time() + 10
    while time.time() < t_end:
        arduino_ports = [ # Find all the ports with "IOUSBHostDevice" as its tag
            p.device
            for p in serial.tools.list_ports.comports()
            if 'IOUSBHostDevice' in p.description   # IOUSBHostDevice is the arduino's tag or something, the serial value changes for each mac so we cannot search using that
        ]
        if not arduino_ports: #Loops until arduino is found
            continue
        else:        
            if len(arduino_ports) > 1:
                print('Multiple controllers found - using the first')
            else:
                # print("Controller found.", end =" ") # Arduino is found
                return [True, serial.Serial(arduino_ports[0], 115200, timeout=.1)] #initialize connection with arduino
            break #Break out of the loop once the arduino is found 
    print("Arduino not found")

def emulator(arduino,placeholder,newdata):
    if arduino[0]:
        while True:
            newdata=[]
            data = (arduino[1].readline()).split(" ") #Read the data receiveda from the arduino
            del data[-1]
            for i in range(len(data)):
                data[i] = int(data[i]) #converts every value into int
                newdata.append(selectedKeys[data[i]]) #converts into keypress + appends into a string
            if placeholder != newdata:
                if placeholder != newdata:
                    for j in placeholder:
                        pyautogui.keyUp(j) #keyup if no input detected + if placeholder has a previous input
                    print("up: " + str(placeholder) + "\n")
                    for k in newdata:
                        pyautogui.keyDown(k) #keyup ssdddddif no input detected + if placeholder has a previous input
                    print("down: " + str(newdata) + "\n")
                    placeholder = newdata
                # print(placeholder)
                # print(newdata)
                # print("change")
                # for j in placeholder:
                #     pyautogui.keyUp(j) #keyup if no input detected + if placeholder has a previous input
                #     # print("up: " + j + "\n")
                # for k in newdata:
                #     pyautogui.keyDown(k) #keyup no input detected + if placeholder has a previous input
                #     # print("down: " + k + "\n")
                # placeholder = newdata
                # newdata = []
    else:
        print('''Controller connection not found. 
        Common troubleshooting procedures:
        - Unplug the controller and plug it back in
        - Press the "Find controller" button
        - Close any other application that uses serial communication with the arduino in the controller
''')
    




while True:
    action = int(input("Enter selected action: "))
    if action == 0:
        try:
            arduino = searchArduino()
        except Exception as exception:
            print("However, that controller is being used by another application. Try closing any other application that uses serial communication with the arduino in the controller.")
            arduino[0] = False
        print("")
    elif action == 1:
        emulator(arduino,placeholder,newdata)
    else:
        break


