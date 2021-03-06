import tkinter 

#enable = PortDataEmulation.sendEnable() #[X,X,X,X,X] where X is 1/0
keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","[","]","\\",";","'",",",".","/","up","down","left","right"] #The list of all possible keys
selectedKeys = ["w","a","s","d","esc"] # the keys that are currently selected, cuztomisable list
root = tkinter.Tk() #Open New Window
root.title('Enter your Keys')

def syncToArduino(): #opens window when syncing to arduino
    syncArduino = tkinter.Toplevel() #Open New Window
    #states: 0 = not found, 1 = found, 2 = loading
    state = 0 #to be deleted
    #changing the outputs of different states
    if state == 0: #when no controller is found
        syncArduino.title("Controller Status: Not Found")
        stateLabel = tkinter.Label(syncArduino, text="Controller Status: Not Found")
        #troubleshooting tips
        troubleshootLabel = tkinter.Label(syncArduino, text='Common troubleshooting procedures:\n- Unplug the controller and plug it back in\n- Press the "Find controller" button\n- Close any other application that uses serial communication with the arduino in the controller') #shows what showChoices means
        troubleshootLabel.grid(row=1,column=0)
    elif state == 1: #when controller is found
        syncArduino.title("Controller Status: Found!")
        stateLabel = tkinter.Label(syncArduino, text="Controller Status: Found!")
    elif state == 2: #when still looking for controller
        syncArduino.title("Controller Status: Finding...")
        stateLabel = tkinter.Label(syncArduino, text="Controller Status: Finding...")
    stateLabel.grid(row=0,column=0)

def startController():
    controller = tkinter.Toplevel() #Open New Window
    controller.title("Controller")

    start = tkinter.Button(controller, text="Start Controller",command=None) #Btn to start the controller
    stop = tkinter.Button(controller, text="Stop Controller",command=None) #Btn to stop the controller

    start.grid(row=0,column=0)    
    stop.grid(row=0,column=1)
helpwindow = tkinter.Label(root, text=keys)
helpwindow.grid(row=3,column=3)

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
    showChoices.config(text=selectedKeys) #shows all the currently selected keys
    showChoices.grid(row=7,column=1)


button1 = tkinter.StringVar()#Change to String
button1.set('w') #Default Key1
button1 = tkinter.Entry(root,text="Enter First Button") #Enter button1
btnLabel1 = tkinter.Label(root, text="First Button") #Show what is button1
btnLabel1.grid(row=2,column=0)
button1.grid(row=2,column=1)


button2 = tkinter.StringVar()
button2.set('a') #Default Key2
button2 = tkinter.Entry(root,text="Enter Second Button") #Enter button2
btnLabel2 = tkinter.Label(root, text="Second Button") #Show what is button2
btnLabel2.grid(row=3,column=0)
button2.grid(row=3,column=1)

button3 = tkinter.StringVar()
button3.set('s') #Default Key3
button3 = tkinter.Entry(root,text="Enter Third Button") #Enter button3
btnLabel3 = tkinter.Label(root, text="Third Button") #Show what is button3
btnLabel3.grid(row=4,column=0)
button3.grid(row=4,column=1)

button4 = tkinter.StringVar()
button4.set('d') #Default Key4
button4 = tkinter.Entry(root,text="Enter Fourth Button") #Enter button1
btnLabel4 = tkinter.Label(root, text="Fourth Button") #Show what is button4
btnLabel4.grid(row=5,column=0)
button4.grid(row=5,column=1)

button5 = tkinter.StringVar()
button5.set('esc') #Default Key4
button5 = tkinter.Entry(root,text="Enter Fifth Button") #Enter button1
btnLabel5 = tkinter.Label(root, text="Fifth Button") #Show what is button5
btnLabel5.grid(row=6,column=0)
button5.grid(row=6,column=1)

arduinoSyncBtn = tkinter.Button(root, text="Sync the Device",command=syncToArduino) #Btn to open window to sync to arduino
arduinoSyncBtn.grid(row=0,column=0)

startControllerBtn = tkinter.Button(root, text="Start Controller",command=startController) #Btn to open window to sync to arduino
startControllerBtn.grid(row=0,column=1)

choicesLabel = tkinter.Label(root, text="Selected keys:") #shows what showChoices means

choiceButton = tkinter.Button(root, text="Confirm selection",command=getKeyInput) #Btn to set the selectedKeys
choiceButton.grid(row=8,column=0,columnspan=2)
showChoices = tkinter.Label(root, text=selectedKeys) #shows all the currently selected keys
choicesLabel.grid(row=7,column=0)
showChoices.grid(row=7,column=1)



root.mainloop() #Loop forever/stay in window