# 2022-Computing-Coursework

## File Organisation
### Testing
[Stage 1](https://github.com/Shanjiith-Pranov/2022-Computing-Coursework/tree/main/Testing/Stage%201) and [Stage 2](https://github.com/Shanjiith-Pranov/2022-Computing-Coursework/tree/main/Testing/Stage%202) represents the different stages in our code development.
### Main 
[Main](https://github.com/Shanjiith-Pranov/2022-Computing-Coursework/tree/main/main) contains the final stage of code.
### Deployment
[Deployment]() contains the code to be zipped and released.

## Installation
## Installing Dependencies:
```
python<your python version> -m pip install pyautogui
python<your python version> -m pip install pyserial
python<your python version> -m pip install tk
```
## Running the code
Downlad the zip the file from the [releases](https://github.com/Shanjiith-Pranov/2022-Computing-Coursework/releases/new). Unzip the file and open `main.py` in your choice of editor(IDLE for teachers testing this code). Run the code.
## Testing the program
- First, connect the controller to the machine you are running the code on.
- Next, press `Sync the Device`. The programm will search for a connected controller for 10 seconds.
- If the controller is not found, follow the instructions shown
- After the controller is found, press the `Run arduino` button. The button should turn blue.
- If you would like to remap a key, press the the `Run arduino` button again and wait for it to turn grey to stop the controller. Now, change the key for the respective button and hit `Confirm selection`.
- If you would like to change a macro, press the the `Run arduino` button again and wait for it to turn grey to stop the controller. Now, open the file `macros.txt` and make changes to the existing macros. After editing, save the file and close it. Remeber to make sure that there are only 2 lines in the file.
## Troubleshooting
### "Python" would like to control this computer using accessibility features.
If you see this warning: ![](https://github.com/Shanjiith-Pranov/2022-Computing-Coursework/blob/main/warning.jpg)
Click `Open System Preferences`. Click the lock icon and enter your password. Click `Accessibility` in the left column. Click the checkmark beside `Python`.
![](https://github.com/Shanjiith-Pranov/2022-Computing-Coursework/blob/main/system_preferences.jpg)
### Loading for while (Beach ball of death)
- The loading maybe caused because your computer is lagging or the programm is running in the background but there is no text field to input the keys into. Please wait for a while or quit(or force quit) the app and reopen. 
- Another cause of the problem is trying to change the keys while the controller is running. Close the app and reopen it. When changing keys remember to stop the controller first.

## Physical Prototype
### Pictures
You can find the pictures of our prototype [here](https://github.com/Shanjiith-Pranov/2022-Computing-Coursework/tree/main/Prototype%20pictures)
### Notes when testing the physical prototype
- The prototype is fragile, please be gentle with it
- Even though the usage of feet to press the buttons is stated, please do not use your feet to test the prototype as it may break the prototype

## Modules used
### Python
- [pyserial](https://github.com/pyserial/pyserial)
- [pyautogui](https://github.com/asweigart/pyautogui)
- [tkinter](https://docs.python.org/3/library/tk.html)

## References
### Tkinter 
- https://www.youtube.com/watch?v=YXPyB4XeYLA 
- https://realpython.com/python-gui-tkinter/ 
- https://stackoverflow.com/questions/44588154/python-tkinter-how-to-config-a-button-that-was-generated-in-a-loop
- https://stackoverflow.com/questions/7573031/when-i-use-update-with-tkinter-my-label-writes-another-line-instead-of-rewriti
- https://www.tutorialspoint.com/python/tk_button.htm

### Arduino
- https://create.arduino.cc/projecthub/smart-tech/programming-arduino-using-python-f3d2c0
- https://realpython.com/arduino-python/
- https://realpython.com/arduino-python/#reading-digital-inputs
- https://github.com/mattiasjahnke/arduino-projects/tree/master/arduino-pc-joystick	
- https://stackoverflow.com/questions/24214643/python-to-automatically-select-serial-ports-for-arduino	
