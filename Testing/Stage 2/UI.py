import tkinter 
#import PortDataEmulation
i = True
keys = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","[","]","\\",";","'",",",".","/","up","down","left","right"] #The list of all possible keys
selectedKeys = ["w","a","s","d","esc"] # the keys that are currently selected, cuztomisable list
root = tkinter.Tk()
root.title('Enter your Keys ')
def open():
    top = tkinter.Toplevel() #Open New Window
    top.title("Syncing the Device")
def show():
    ChoiceLabel = tkinter.Label(root, text=selectedKeys).pack()

#enable = PortDataEmulation.sendEnable() #[X,X,X,X,X] where X is 1/0
# Dropdown window
clicked1 = tkinter.StringVar()#Change to String
clicked1.set('w') #Default Key1
clicked2 = tkinter.StringVar()
clicked2.set('a') #Default Key2
clicked3 = tkinter.StringVar()
clicked3.set('s') #Default Key3
clicked4 = tkinter.StringVar()
clicked4.set('d') #Default Key4
clicked5 = tkinter.StringVar()
clicked5.set('esc') #Default Key4

WindowButton = tkinter.Button(root, text="Sync the Device",command=open) #Btn to open window
WindowButton.grid(row=0,column=3)



drop1 = tkinter.OptionMenu(root,clicked1,*keys) #Drop Down Menu for button1
drop1.grid(row=0,column=1)
Label1 = tkinter.Label(root, text="First Button") #Show what is button1
Label1.grid(row=0,column=0)

drop2 = tkinter.OptionMenu(root,clicked2,*keys) #Drop Down Menu for button2
drop2.grid(row=1,column=1)
Label2 = tkinter.Label(root, text="Second Button") #Show what is button2
Label2.grid(row=1,column=0)

drop3 = tkinter.OptionMenu(root,clicked3,*keys) #Drop Down Menu for button3
drop3.grid(row=2,column=1)
Label3 = tkinter.Label(root, text="Third Button") #Show what is button3
Label3.grid(row=2,column=0)

drop4 = tkinter.OptionMenu(root,clicked4,*keys) #Drop Down Menu for button4
drop4.grid(row=3,column=1)
Label4 = tkinter.Label(root, text="Fourth Button") #Show what is button4
Label4.grid(row=3,column=0)

drop5 = tkinter.OptionMenu(root,clicked5,*keys) #Drop Down Menu for button4
drop5.grid(row=4,column=1)
Label5 = tkinter.Label(root, text="Fifth Button") #Show what is button4
Label5.grid(row=4,column=0)

ChoiceButton = tkinter.Button(root, text="Confirm selection",command=show) #Btn to set the selectedKeys
ChoiceButton.grid(row=5,column=0)
while i == True:
    choice1 = clicked1.get()
    choice2 = clicked2.get()
    choice3 = clicked3.get()
    choice4 = clicked4.get()
    choice5 = clicked5.get()
    print(choice1,choice2,choice3,choice4,choice5)
    break

root.mainloop() #Loop forever/stay in window


