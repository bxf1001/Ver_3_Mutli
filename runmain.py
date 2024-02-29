import json
import datetime
import subprocess
from time import sleep
from whatsapp import WhatsApp
from pywinauto.keyboard import send_keys
import PySimpleGUI as sg
import concurrent.futures
from pywinauto import Application

class Runmain:

    def __init__(self) -> None:
        try:
            with open('user_data.json', 'r') as f:
                self.user_data = json.load(f)
        except FileNotFoundError:
            # If the file doesn't exist, start with an empty dictionary
            self.user_data = {}

    def store_data(self):
        user_id = input("Enter User ID: ")
        if user_id in self.user_data: 
            print("User already exists.")
        else:
            value1 = input("Enter No1: ")
            value2 = input("Enter No2: ")
            value3 = input("Enter No3: ")
            self.user_data[user_id] = {'1': value1, '2': value2, '3': value3}
        # Write the updated data to the file
            with open('user_data.json', 'w') as f:
                json.dump(self.user_data, f,indent=4)

    def retrieve_data(self):
        enter_calls = input("Choose Calls (1/2): ")
    
        if enter_calls=='1':
            user_id = input("Enter User ID: ")
            if user_id in self.user_data:
                print("choose (1, 2, or 3):", self.user_data[user_id])
                field = input("Enter field to print (or 'all' to print all fields): ")
                if field.lower() == 'all':
                    print(self.user_data[user_id])
                elif field in self.user_data[user_id]:
                    self.add_time=float(input("enter time:: "))
                    if self.add_time<=12:

                        wa=WhatsApp(self.user_data[user_id][field],self.add_time)
                        wa.run_method()
                        add_timer1 = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                        print(f"{self.user_data[user_id][field]} (Called at {add_timer1})")
                        timestamped_data = {
                            "user_id": user_id,
                            "field": field,
                            "number": self.user_data[user_id][field],
                            "timestamp": add_timer1
                        }
                        with open('timestamped_data.json', 'a') as f:
                            json.dump(timestamped_data, f)
                            f.write('\n')  # Add a newline for readability
                    else:
                        print("Time Limit Can't Exceed more than 10 Min")
                    
                else:
                    print("Invalid Field")
            else:
                print("User not found.")
      
        if enter_calls=='2':
            user_id = input("Enter User ID: ")
            if user_id in self.user_data:
                print("choose (1, 2, or 3):", self.user_data[user_id])
                field1 = input("Enter field to print (or 'all' to print all fields): ")
                field2 = input("Enter field to print (or 'all' to print all fields): ")
                if field1  in self.user_data[user_id]:
                    self.add_time1=float(input("enter time:: "))
                    self.add_time2=12-self.add_time1
                    wa=WhatsApp(self.user_data[user_id][field1],self.add_time1)
                    wa.run_method() 
                    add_timer2 = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    print(f"{self.user_data[user_id][field1]} (Called at {add_timer2})")

                # Create a new dictionary to store timestamped data
                    timestamped_data = {
                        "user_id": user_id,
                        "field": field1,
                        "number": self.user_data[user_id][field2],
                        "timestamp": add_timer2
                    }
                    with open('timestamped_data.json', 'a') as f:
                        json.dump(timestamped_data, f)
                        f.write('\n')  # Add a newline for readability
                    sleep(1)
                    send_keys("^%{VK_NUMPAD0}")
                    sleep(3)
                    wa=WhatsApp(self.user_data[user_id][field2],self.add_time2)
                    wa.run_method()
                    add_timer3 = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    print(f"{self.user_data[user_id][field2]} (Called at {add_timer3})")
                    timestamped_data = {
                        "user_id": user_id,
                        "field": field2,
                        "number": self.user_data[user_id][field2],
                        "timestamp": add_timer3
                    }
                # Write the timestamped data to a new file
                    with open('timestamped_data.json', 'a') as f:
                        json.dump(timestamped_data, f)
                        f.write('\n')  # Add a newline for readability
                else:
                    print("Invalid field.")
            else:
                print("User not found.")
        else:
            print("invalid option")  
    def print_timestamped_data(self,user_id): 
        try:
            with open('timestamped_data.json', 'r') as f:
                data_found = False  # Flag to track if data exists for the user ID
                for line in f:
                    entry = json.loads(line)  # Parse each line as a separate JSON object
                    if entry['user_id'] == user_id:
                        print("-------------------------------------             ")
                        print(f"User ID: {entry['user_id']}")
                        print(f"Field: {entry['field']}")
                        print(f"Value: {entry['number']}")  # Corrected key name
                        print(f"Timestamp: {entry['timestamp']}\n")
                        print("-------------------------------------             ")
                        data_found = True  # Data exists for the specified user ID
                if not data_found:
                    print("No data found for the specified user ID.")
        except FileNotFoundError:
            print("No timestamped data file found.")
# Example usage:
    def run_main(self):
        while True:
            print("         -------------------------------------             ")
            print("             WELCOME TO PUZHAL PHONE PORTAL              ")
            print("           ----------------------------------             ")
            print("\n1. Store Data\n2. Make Call\n3. Search Data\n4. Quit")
            option = input("Enter your option: ")
            if option == '1':
                self.store_data()
            elif option == '2':
                self.retrieve_data()
            elif option == '3':
                user_id_input = input("Enter User ID to retrieve data: ")
                self.print_timestamped_data(user_id_input)
            elif option == '4':
                break
            else:
                print("Invalid option. Please try again.")
 
    def check_group_call(self):
        self.dialog = self.appwhatsapp.window(title="Group video call ‎- WhatsApp", control_type="Window")
        self.trigger= self.dialog.child_window(title="Group video call ‎- WhatsApp", auto_id="TitleBar", control_type="Window")
        count_down= 0

        while count_down<self.timer:
           sleep(1)
           print("Function 1 executed")
           try: 
                if self.trigger.is_enabled():
                    sg.theme('NeutralBlue')
                    sg.popup('Conference Not Allowed',font='stencil 50')
                    break 
           except:
                sleep(1)
                continue
           count_down +=1

    def main_reject(self):
        app = Application(backend='uia').start(r"cmd.exe /c start shell:appsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App", create_new_console=True, wait_for_idle=False)
        sleep(3)
        app = Application(backend='uia').connect(title_re="WhatsApp")
        dialog = app.window(title="Group video call ‎- WhatsApp", control_type="Window")
        button = dialog.child_window(title="Group video call ‎- WhatsApp", auto_id="TitleBar", control_type="Window")
        count_down = 0
        while count_down<self.add_time or self.add_time1 or self.add_time2:
            try:
                if button.is_enabled():
                    sleep(2) 
                    sg.theme('NeutralBlue')
                    sg.popup('Conference Not Allowed',font='stencil 50')
                    sleep(3)
                    subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)
                    sleep(1)
                    send_keys("^%{VK_NUMPAD0}")
                    sleep(1)
                    send_keys("{VK_F12}")
                    sleep(1)
                    send_keys("^%{VK_NUMPAD0}")
                    break  # Button is enabled, so click it and exit the loop
                    # Button is enabled, so click it and exit the loop
            except:
                sleep(1)
                continue
            counnt_down +=1


if __name__ == "__main__":

    run = Runmain()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit both methods for execution
        future1 = executor.submit(run.run_main)
        future2 = executor.submit(run.main_reject)

        # Wait for both methods to complete
        concurrent.futures.wait([future1, future2])

