from time import sleep
import tkinter 
from tkinter import ttk
import main

keys = ["macro_1","macro_2","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","[","]","\\",";","'",",",".","/","up","down","left","right","esc","space"] #The list of all possible keys
selectedKeys = ["w","a","s","d","esc"] # the keys that are currently selected, cuztomisable list

## Hern Yee + Darius/Setup 
root = tkinter.Tk() # Open New Window
root.title('Enter your Keys')
root.tk.call("source", "azure.tcl") # Setting the theme
root.tk.call("set_theme", "dark")
## Darius + Hern Yee/opens window when syncing to arduino
def syncToArduino(): 
    syncArduino = tkinter.Toplevel() # Open New Window

    main.Search()

    syncArduino.title("Controller Status: Loading...") # Creating a new window

    sleep(1) # Sleep while loading
    # states: 0 = not found, 1 = found, 2 = loading
    arduino = open("arduino.txt", "r") # Opening arduino.txt to fetch state
    state = int(arduino.readline()) # Fetching data from arduino.txt
    arduino.close()

    # Changing the outputs of different states
    if state == 0: # When no controller is found
        syncArduino.title("Controller Status: Not Found") # Creating a new window
        stateLabel = tkinter.Label(syncArduino, text="Controller Status: Not Found") # Renaming the state to "not found"
        arduinoSyncLbl.config(text="Controller Status: Not Found") # Adding a label to the new window
        # Troubleshooting tips
        troubleshootLabel = tkinter.Label(syncArduino, text='Common troubleshooting procedures:\n- Unplug the controller and plug it back in\n- Press the "Find controller" button\n- Close any other application that uses serial communication with the arduino in the controller') #shows some troubleshooting tips
        troubleshootLabel.grid(row=1,column=0)

    elif state == 1: # When controller is found
        arduinoSyncLbl.config(text="Controller Status: Found") # Adding a label to the new window
        syncArduino.title("Controller Status: Found!") # Renaming the state to "found"
        stateLabel = tkinter.Label(syncArduino, text="Controller Status: Found!")
    stateLabel.grid(row=0,column=0)
## Darius + Hern Yee + Shanjiith
def emulator():
    arduinoValue = open("arduino.txt", "r") # Opening arduino.txt to fetch state
    toggle = open("toggle.txt", "r") # Opening arduino.txt to fetch state
    if int(arduinoValue.readline())  == 1 and int(toggle.readline())  == 1:
        main.emulator()
        root.after(0, emulator)    

## Darius + Hern Yee + Shanjiith/ Checks if controller is connected + starts the controller
def startController(): 
    arduino = open("arduino.txt", "r") # Opening arduino.txt to fetch state
    state = int(arduino.readline()) # Fetching data from arduino.txt
    arduino.close()

    ## Darius + Shanjiith
    if state == 0: # If an arduino is NOT connected: run this
        syncArduino = tkinter.Toplevel() # Open New Window
        syncArduino.title("Controller Status: Not Found")
        stateLabel = tkinter.Label(syncArduino, text="Controller Status: Not Found")
        # Troubleshooting tips
        troubleshootLabel = tkinter.Label(syncArduino, text='Common troubleshooting procedures:\n- Unplug the controller and plug it back in\n- Press the "Find controller" button\n- Close any other application that uses serial communication with the arduino in the controller') #shows what showChoices means
        troubleshootLabel.grid(row=1,column=0)
        stateLabel.grid(row=0,column=0)

    ## Darius + Shanjiith
    elif state == 1: # If an arduino is connected: run this
        main.StartStop()
          
        toggle = open("toggle.txt", "r") # Opening arduino.txt to fetch state
        toggleValue = int(toggle.readline()) # Fetching data from arduino.txt
        toggle.close()    
        sleep(2)
        if toggleValue == 1: # Runs code if toggle is on
            emulator()
        elif toggleValue == 0: # Else, pass
            pass
        startControllerBtn.grid(row=0,column=1)

## Darius + Hern Yee
def getKeyInput(): # Updates the selected keys when Confirm Selection is pressed
    # Updates the value of each key when Confirm Selection is pressed
    selectedKeys[0] = button1.get() 
    selectedKeys[1] = button2.get()
    selectedKeys[2] = button3.get()
    selectedKeys[3] = button4.get()
    selectedKeys[4] = button5.get()
    
    data = open("keys.txt",'w') # Saves selectedKeys into a text file
    for i in range(len(selectedKeys)): # Splits selected keys up
        data.write(selectedKeys[i] + " ")
    data.close()
    # Updates the label every time Confirm Selection is pressed
    showChoices.config(text=selectedKeys) # Shows all the currently selected keys
    showChoices.grid(row=7,column=1)

## Hern Yee/ Dropdown windows
button1 = tkinter.StringVar() # Change to String
button1.set('w') # Default Key1
drop1 = tkinter.OptionMenu(root,button1,*keys) # Drop Down Menu for button1
btnLabel1 = tkinter.Label(root, text="First Button") # Show what is button1
btnLabel1.grid(row=2,column=0)
drop1.grid(row=2,column=1)

button2 = tkinter.StringVar()
button2.set('a') # Default Key2
drop2 = tkinter.OptionMenu(root,button2,*keys) # Drop Down Menu for button2
btnLabel2 = tkinter.Label(root, text="Second Button") # Show what is button2
btnLabel2.grid(row=3,column=0)
drop2.grid(row=3,column=1)

button3 = tkinter.StringVar()
button3.set('s') # Default Key3
drop3 = tkinter.OptionMenu(root,button3,*keys) # Drop Down Menu for button3
btnLabel3 = tkinter.Label(root, text="Third Button") # Show what is button3
btnLabel3.grid(row=4,column=0)
drop3.grid(row=4,column=1)

button4 = tkinter.StringVar()
button4.set('d') # Default Key4
drop4 = tkinter.OptionMenu(root,button4,*keys) # Drop Down Menu for button4
btnLabel4 = tkinter.Label(root, text="Fourth Button") # Show what is button4
btnLabel4.grid(row=5,column=0)
drop4.grid(row=5,column=1)

button5 = tkinter.StringVar()
button5.set('esc') # Default Key4
drop5 = tkinter.OptionMenu(root,button5,*keys) # Drop Down Menu for button5
btnLabel5 = tkinter.Label(root, text="Fifth Button") # Show what is button5
btnLabel5.grid(row=6,column=0)
drop5.grid(row=6,column=1)

## Darius + Hern Yee/setting up the other buttons
arduinoSyncBtn = ttk.Button(root, text="Sync the Device",style='Toggle.TButton', command=syncToArduino) # Btn to open window to sync to arduino
arduinoSyncLbl = tkinter.Label(root,text="Controller Status: Not Found") # Shows current state of arduino
arduinoSyncLbl.grid(row=1,column=0,columnspan=2)
arduinoSyncBtn.grid(row=0,column=0)

startControllerBtn = ttk.Button(root, text="Run Controller",style='Toggle.TButton', command=startController) # Btn to open window to sync to arduino
startControllerBtn.grid(row=0,column=1)

choicesLabel = tkinter.Label(root, text="Selected keys:") # Shows what showChoices means
choiceButton = ttk.Button(root, text="Confirm selection",style='Accent.TButton', command=getKeyInput) # Btn to set the selectedKeys
showChoices = tkinter.Label(root, text=selectedKeys) # Shows all the currently selected keys
choicesLabel.grid(row=7,column=0)
showChoices.grid(row=7,column=1)
choiceButton.grid(row=8,column=0,columnspan=2)   
root.mainloop() # Loop forever/stay in window