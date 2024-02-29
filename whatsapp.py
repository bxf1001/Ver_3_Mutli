import subprocess
import PySimpleGUI as sg
import time
import subprocess
from time import sleep
from pywinauto import Application
from pywinauto.keyboard import send_keys
from AppOpener import open
import numpy as np
from pynput import keyboard




class WhatsApp:

    


    def __init__(self,number,timer):
        self.timer = int(timer*60)
        self.number=number
        self.runbandicam=open("Bandicam")
        self.key= KeyListener()
        
    def run_method(self):
        self._precheck_events()
        self._postcheck_events()


    def _precheck_events(self):
        self.start_applications_py()
        sleep(1)
        self.get_phonenumber()
        sleep(1)
        self.click_call_button()
        self.start_recording()
        sleep(1)
        self.lock_screen()

    def _postcheck_events(self):
        self.timer_count()
        self.click_end_button()
        sleep(1)
        self.unlock_screen()
        sleep(1)
        self.stop_recording()
        sleep(1)
        self.lock_screen()


    def start_applications_py(self):
        sleep(3)
        self.startapp = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)
        sleep(1)
        self.appwhatsapp = Application(backend='uia').connect(title_re="WhatsApp")

    def get_phonenumber(self):
        sleep(0.25)
        self.url = f"whatsapp://send?phone=+91{self.number}"
        self.subwhatsapp=subprocess.Popen(["cmd", "/C", f"start {self.url}"], shell=True)
        sleep(0.25)
        self.url = f"whatsapp://send?phone=+91{self.number}"
        self.subwhatsapp=subprocess.Popen(["cmd", "/C", f"start {self.url}"], shell=True)
    
    
    
    def start_recording(self):
        self.dialog = self.appwhatsapp.window(title="Video call ‎- WhatsApp")
        self.button = self.dialog.child_window(title="Add members", auto_id="ParticipantSideBarTriggerButton", control_type="Button")
        while True:
            try:
                if self.button.is_enabled():
                    send_keys("{VK_F12}")
                    break 
            except:
                time.sleep(1)
                continue

    def stop_recording(self):
        sleep(1)
        if self.timer<720:
            send_keys("{VK_F12}")

    def lock_screen(self):
        sleep(1)
        send_keys("^%{VK_NUMPAD0}")

    def unlock_screen(self):
        sleep(1)
        send_keys("^%{VK_NUMPAD0}")
    
    def click_call_button(self):
        while True:
            try:
                self.appwhatsapp.WhatsAppDialog.child_window(title="Video call", auto_id="VideoCallButton", control_type="Button").click()
                break
            except:
                time.sleep(1)
                continue


    def click_end_button(self):  
        try: 
            self.appwhatsapp.Dialog.child_window(title="End call", auto_id="EndCallButton", control_type="Button").click()   
        except:
            subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)

    def check_group_call(self):
        self.dialog = self.appwhatsapp.window(title="Group video call ‎- WhatsApp", control_type="Window")
        self.trigger= self.dialog.child_window(title="Group video call ‎- WhatsApp", auto_id="TitleBar", control_type="Window")
        while True:
           try: 
                if self.trigger.is_enabled():
                    sg.theme('NeutralBlue')
                    sg.popup('Conference Not Allowed',font='stencil 50')
                    break 
           except:
                time.sleep(1)
                continue

    def timer_count(self):
        count_down = 0  
        #for _ in range(time_period):
            #sleep(1)  # Wait for 1 second 
        while count_down<self.timer:
            time.sleep(1)
            self.key.start()
            count_down += 1

class KeyListener:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.keys_to_listen = {'space'}  # Add more keys here if needed

    def on_press(self, key):
        try:
            key_char = key.char  # Get the character representation of the key
            if key_char in self.keys_to_listen:
                print(f"{key_char} key pressed. Exiting the program.")
                return False  # Stop listening
        except AttributeError:
            pass

    def start(self):
        print("Press the space bar or 'a' key to break:")
        self.listener.start()
        self.listener.join()

if __name__ == "__main__":
    key_listener = KeyListener()
    key_listener.start()
