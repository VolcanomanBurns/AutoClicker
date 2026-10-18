#Set up
import time
import threading

from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


#Set Variables and HotKeys
d = 0.0000001
btn = Button.left

start_key = KeyCode(char='a')
exit_key = KeyCode(char='b')


#Running in background
class AutoClicker(threading.Thread):
    def __init__(self, d, btn):
        super().__init__()
        self.d = d                 #Delay
        self.btn = btn             #Button
        self.clicking = False
        self.active = True

    def start_click(self):
        self.clicking = True

    def stop_click(self):
        self.clicking = False

    def run(self):
        while self.active:
            while self.clicking:
                mouse.click(self.btn)
                time.sleep(self.d)



#Create a controller to sim mouse actions
mouse = Controller()

clicker = AutoClicker(d, btn)
clicker.start()


#Listen for Key Presses
def on_press(k):
    if k == start_key:
        if clicker.clicking:
            clicker.stop_click()
            print("[INFO] Clicker Stopped.")
        else:
            clicker.start_click()
            print("[INFO] Clicker Started.")
    elif k == exit_key:
        clicker.exit()
        print("[INFO] Exiting.")
        return False  # Stop Listener



#Keyboard Listener
with Listener(on_press=on_press) as listener:
    listener.join()

