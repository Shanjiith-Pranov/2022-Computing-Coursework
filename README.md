# 2022-Computing-Coursework

## File Organisation
### Testing
[Stage 1](https://github.com/Shanjiith-Pranov/2022-Computing-Coursework/tree/main/Testing/Stage%201) and [Stage 2](https://github.com/Shanjiith-Pranov/2022-Computing-Coursework/tree/main/Testing/Stage%202) represents the different stages in our code development.
### Main 
[Main]() contains the final "deployment-ready" code.<sub><sup><sub><sup><sub><sup><sub><sup><sub><sup><sub><sup><sub><sup><sub><sup>_What else did you expect?_</sup></sub></sup></sub></sup></sub></sup></sub></sup></sub></sup></sub></sup></sub></sup></sub>

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
- If you would like to remap a key, press the the `Run arduino` button again and wait for it to turn grey. Now, change the key for the respective button and hit `Confirm selection`.
## Troubleshooting
### "Python" would like to control this computer using accessibility features.
If you see this warning: ![](https://github.com/Shanjiith-Pranov/2022-Computing-Coursework/blob/main/warning.jpg)
Click `Open System Preferences`. Click the lock icon and enter your password. Click `Accessibility` in the left column. Click the checkmark beside `Python`.
![](https://github.com/Shanjiith-Pranov/2022-Computing-Coursework/blob/main/system_preferences.jpg)
### Loading for while (Beach ball of death)
- The loading maybe caused because your computer is lagging or the programm is running in the background but there is no text field to input the keys into. Please wait for a while or quit the app and reopen. 
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
