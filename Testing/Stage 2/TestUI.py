import tkinter 

keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","[","]","\\",";","'",",",".","/","up","down","left","right"] #The list of all possible keys
selectedKeys = ["w","a","s","d","esc"] # the keys that are currently selected, cuztomisable list

root = tkinter.Tk()
root.title('Enter your Keys')

def syncToArduino(): #opens window when syncing to arduino
    syncArduino = tkinter.Toplevel() #Open New Window
    syncArduino.title("Syncing to the device...")

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
    showChoices.grid(row=4,column=3)

#enable = PortDataEmulation.sendEnable() #[X,X,X,X,X] where X is 1/0

# Dropdown window
button1 = tkinter.StringVar()#Change to String
button1.set('w') #Default Key1
button2 = tkinter.StringVar()
button2.set('a') #Default Key2
button3 = tkinter.StringVar()
button3.set('s') #Default Key3
button4 = tkinter.StringVar()
button4.set('d') #Default Key4
button5 = tkinter.StringVar()
button5.set('esc') #Default Key4

windowButton = tkinter.Button(root, text="Sync the Device",command=syncToArduino) #Btn to open window to sync to arduino
windowButton.grid(row=0,column=3)

choiceLabel = tkinter.Label(root, text="Selected keys:") #shows what showChoices means
showChoices = tkinter.Label(root, text=selectedKeys) #shows all the currently selected keys
choiceLabel.grid(row=3,column=3)
showChoices.grid(row=4,column=3)

drop1 = tkinter.OptionMenu(root,button1,*keys) #Drop Down Menu for button1
btnLabel1 = tkinter.Label(root, text="First Button") #Show what is button1
drop1.grid(row=0,column=1)
btnLabel1.grid(row=0,column=0)

drop2 = tkinter.OptionMenu(root,button2,*keys) #Drop Down Menu for button2
btnLabel2 = tkinter.Label(root, text="Second Button") #Show what is button2
drop2.grid(row=1,column=1)
btnLabel2.grid(row=1,column=0)

drop3 = tkinter.OptionMenu(root,button3,*keys) #Drop Down Menu for button3
btnLabel3 = tkinter.Label(root, text="Third Button") #Show what is button3
drop3.grid(row=2,column=1)
btnLabel3.grid(row=2,column=0)

drop4 = tkinter.OptionMenu(root,button4,*keys) #Drop Down Menu for button4
btnLabel4 = tkinter.Label(root, text="Fourth Button") #Show what is button4
drop4.grid(row=3,column=1)
btnLabel4.grid(row=3,column=0)

drop5 = tkinter.OptionMenu(root,button5,*keys) #Drop Down Menu for button5
btnLabel5 = tkinter.Label(root, text="Fifth Button") #Show what is button5
drop5.grid(row=4,column=1)
btnLabel5.grid(row=4,column=0)

choiceButton = tkinter.Button(root, text="Confirm selection",command=getKeyInput) #Btn to set the selectedKeys
choiceButton.grid(row=5,column=0)

root.mainloop() #Loop forever/stay in window