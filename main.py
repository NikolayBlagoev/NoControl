from PyQt5.QtWidgets import QApplication, QMainWindow


try:
    import vgamepad as vg
except:
    import win32api
    import subprocess
    
    win32api.MessageBox(0, 'You need to install the missing drivers', 'Missing Drivers')
    subprocess.call('msiexec /i "extras\VIGEM_setup.msi"', shell=False)
    import vgamepad as vg
from ui import Ui_MainWindow
from threading import Thread
from controller import controller
import json 


app = QApplication([])
ui = Ui_MainWindow()
# Create a Qt widget, which will be our window.
window = QMainWindow()
window.show() 

# PLACEHOLDER : 
keys_dict = {
    # "running" : True,
    # "e" : vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    # "Key.space" : vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    # "g" : vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    # "f" : vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
    # "w" : "LUP",
    # "d" : "LRIGHT",
    # "s" : "LDOWN",
    # "a" : "LLEFT",
    # "Key.up" : "RUP",
    # "Key.right" : "RRIGHT",
    # "Key.down" : "RDOWN",
    # "Key.left" : "RLEFT",
    # "1": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB ,
    # "2": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER ,
    # "3": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER ,
    # "4": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB ,
    # "u" : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    # "j" : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    # "h" : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    # "k" : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    # "5" : vg.XUSB_BUTTON.XUSB_GAMEPAD_START
}

# ACTUALLY LOAD IT
with open('default.json') as in_fl:
    keys_dict = json.load(in_fl)
keys_dict["running"] = True
keys_dict["listening"] = False

keys_dict["obj"] = None
keys_dict["key"] = None
keys_dict["prev_key"] = None
btn = ui.setupUi(window, keys_dict)
thr = Thread(target=controller, args=(keys_dict,btn, ui.pushButton.start_stop,))
keys_dict["Key.backspace"] = vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK 
thr.start()
app.exec()
