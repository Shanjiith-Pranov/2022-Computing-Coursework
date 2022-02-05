import time
import tkinter 
import main #syncing with the arduino

#enable = PortDataEmulation.sendEnable() #[X,X,X,X,X] where X is 1/0

keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","[","]","\\",";","'",",",".","/","up","down","left","right"] #The list of all possible keys
selectedKeys = ["w","a","s","d","esc"] # the keys that are currently selected, cuztomisable list

root = tkinter.Tk() #Open New Window
root.title('Enter your Keys')

def syncToArduino(): #opens window when syncing to arduino
    syncArduino = tkinter.Toplevel() #Open New Window

    syncArduino.title("Controller Status: Loading...")
    stateLabel = tkinter.Label(syncArduino, text="Controller Status: Loading...")
    stateLabel.grid(row=0,column=0)
    time.sleep(10) #ERROR #sleep while loading
    #states: 0 = not found, 1 = found, 2 = loading
    arduino = open("arduino.txt", "r") #opening arduino.txt to fetch state
    state = int(arduino.read()) #fetching data from arduino.txt
    arduino.close()
    #changing the outputs of different states
    if state == 0: #when no controller is found
        syncArduino.title("Controller Status: Not Found")
        stateLabel = tkinter.Label(syncArduino, text="Controller Status: Not Found")
        #troubleshooting tipsb
        troubleshootLabel = tkinter.Label(syncArduino, text='Common troubleshooting procedures:\n- Unplug the controller and plug it back in\n- Press the "Find controller" button\n- Close any other application that uses serial communication with the arduino in the controller') #shows what showChoices means
        troubleshootLabel.grid(row=1,column=0)
    elif state == 1: #when controller is found
        syncArduino.title("Controller Status: Found!")
        stateLabel = tkinter.Label(syncArduino, text="Controller Status: Found!")
    stateLabel.grid(row=0,column=0)

def startController():
    controller = tkinter.Toplevel() #Open New Window
    controller.title("Controller")

    start = tkinter.Button(controller, text="Start Controller",command=None) #Btn to start the controller
    stop = tkinter.Button(controller, text="Stop Controller",command=None) #Btn to stop the controller

    start.grid(row=0,column=0)    
    stop.grid(row=0,column=1)

def getKeyInput(): #updates the selected keys when Confirm Selection is pressed
    #updates the value of each key when Confirm Selection is pressed
    selectedKeys[0] = button1.get() 
    selectedKeys[1] = button2.get()
    selectedKeys[2] = button3.get()
    selectedKeys[3] = button4.get()
    selectedKeys[4] = button5.get()
    #Saves selectedKeys into a text file
    data = open("keys.txt",'w')
    for i in range(len(selectedKeys)): #splits selected keys up
        data.write(selectedKeys[i] + " ")
    data.close()
    #updates the label every time Confirm Selection is pressed
    showChoices = tkinter.Label(root, text=selectedKeys) #shows all the currently selected keys
    showChoices.grid(row=7,column=1)

# Dropdown window

button1 = tkinter.StringVar()#Change to String
button1.set('w') #Default Key1
drop1 = tkinter.OptionMenu(root,button1,*keys) #Drop Down Menu for button1
btnLabel1 = tkinter.Label(root, text="First Button") #Show what is button1
btnLabel1.grid(row=2,column=0)
drop1.grid(row=2,column=1)


button2 = tkinter.StringVar()
button2.set('a') #Default Key2
drop2 = tkinter.OptionMenu(root,button2,*keys) #Drop Down Menu for button2
btnLabel2 = tkinter.Label(root, text="Second Button") #Show what is button2
btnLabel2.grid(row=3,column=0)
drop2.grid(row=3,column=1)

button3 = tkinter.StringVar()
button3.set('s') #Default Key3
drop3 = tkinter.OptionMenu(root,button3,*keys) #Drop Down Menu for button3
btnLabel3 = tkinter.Label(root, text="Third Button") #Show what is button3
btnLabel3.grid(row=4,column=0)
drop3.grid(row=4,column=1)

button4 = tkinter.StringVar()
button4.set('d') #Default Key4
drop4 = tkinter.OptionMenu(root,button4,*keys) #Drop Down Menu for button4
btnLabel4 = tkinter.Label(root, text="Fourth Button") #Show what is button4
btnLabel4.grid(row=5,column=0)
drop4.grid(row=5,column=1)

button5 = tkinter.StringVar()
button5.set('esc') #Default Key4
drop5 = tkinter.OptionMenu(root,button5,*keys) #Drop Down Menu for button5
btnLabel5 = tkinter.Label(root, text="Fifth Button") #Show what is button5
btnLabel5.grid(row=6,column=0)
drop5.grid(row=6,column=1)

placeholderStatus = 0 #DELETE LATER

arduinoSyncBtn = tkinter.Button(root, text="Sync the Device",command=syncToArduino) #Btn to open window to sync to arduino
arduinoSyncLbl = tkinter.Label(root,text=f"Controller Status {placeholderStatus}")
arduinoSyncLbl.grid(row=1,column=0)
arduinoSyncBtn.grid(row=0,column=0)

startControllerBtn = tkinter.Button(root, text="Start Controller",command=startController) #Btn to open window to sync to arduino
startControllerBtn.grid(row=0,column=1)

choicesLabel = tkinter.Label(root, text="Selected keys:") #shows what showChoices means
choiceButton = tkinter.Button(root, text="Confirm selection",command=getKeyInput) #Btn to set the selectedKeys
showChoices = tkinter.Label(root, text=selectedKeys) #shows all the currently selected keys
choicesLabel.grid(row=7,column=0)
showChoices.grid(row=7,column=1)
choiceButton.grid(row=8,column=0,columnspan=2)

root.mainloop() #Loop forever/stay in window