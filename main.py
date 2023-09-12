from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from threading import Thread
import vgamepad as vg
from controller import controller
app = QApplication([])
ui = Ui_MainWindow()
# Create a Qt widget, which will be our window.
window = QMainWindow()
window.show() 
btn = ui.setupUi(window)
keys_dict = {
    "running" : True,
    "e" : vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    "Key.space" : vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    "g" : vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    "f" : vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
    "w" : "LUP",
    "d" : "LRIGHT",
    "s" : "LDOWN",
    "a" : "LLEFT",
    "Key.up" : "RUP",
    "Key.right" : "RRIGHT",
    "Key.down" : "RDOWN",
    "Key.left" : "RLEFT",
    "1": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB ,
    "2": vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER ,
    "3": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER ,
    "4": vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB ,
    "U" : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    "J" : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    "H" : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    "K" : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    "5" : vg.XUSB_BUTTON.XUSB_GAMEPAD_START
}

thr = Thread(target=controller, args=(keys_dict,btn,))
thr.start()
app.exec()
