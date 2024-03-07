import json
import datetime
from time import sleep
import Whatsappcall

from pywinauto.keyboard import send_keys

try:
    with open('user_data.json', 'r') as f:
        user_data = json.load(f)
except FileNotFoundError:
    # If the file doesn't exist, start with an empty dictionary
    user_data = {}

def store_data():
    user_id = input("Enter User ID: ")
    if user_id in user_data: 
        print("User already exists.")
    else:
        value1 = input("Enter No1: ")
        value2 = input("Enter No2: ")
        value3 = input("Enter No3: ")
        user_data[user_id] = {'1': value1, '2': value2, '3': value3}
        # Write the updated data to the file
        with open('user_data.json', 'w') as f:
            json.dump(user_data, f,indent=4)

def retrieve_data():
    enter_calls = input("Choose Calls (1/2/3): ")
    
    if enter_calls=='1':
        user_id = input("Enter User ID: ")
        if user_id in user_data:
            print("choose (1, 2, or 3):", user_data[user_id])
            field = input("Enter field to print (or 'all' to print all fields): ")
            if field.lower() == 'all':
                print(user_data[user_id])
            elif field in user_data[user_id]:
                add_time=float(input("enter time:: "))
                if add_time<=12:

                    Whatsappcall.phone_number(user_data[user_id][field])
                    Whatsappcall.timer(add_time)
                    add_timer1 = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                    print(f"{user_data[user_id][field]} (Called at {add_timer1})")
                    timestamped_data = {
                        "user_id": user_id,
                        "field": field,
                        "number": user_data[user_id][field],
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
        if user_id in user_data:
            print("choose (1, 2, or 3):", user_data[user_id])
            field1 = input("Enter field to print (or 'all' to print all fields): ")
            field2 = input("Enter field to print (or 'all' to print all fields): ")
            if field1  in user_data[user_id]:
                add_time1=float(input("enter time:: "))
                add_time2=12-add_time1
                Whatsappcall.phone_number(user_data[user_id][field1])
                Whatsappcall.timer(add_time1)
                add_timer2 = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print(f"{user_data[user_id][field1]} (Called at {add_timer2})")

            # Create a new dictionary to store timestamped data
                timestamped_data = {
                    "user_id": user_id,
                    "field": field1,
                    "number": user_data[user_id][field1],
                    "timestamp": add_timer2
                }
                with open('timestamped_data.json', 'a') as f:
                    json.dump(timestamped_data, f)
                    f.write('\n')  # Add a newline for readability
                sleep(1)
                send_keys("^%{VK_NUMPAD0}")
                sleep(3)
                Whatsappcall.phone_number(user_data[user_id][field2])
                Whatsappcall.timer(add_time2)
                add_timer3 = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print(f"{user_data[user_id][field2]} (Called at {add_timer3})")
                timestamped_data = {
                    "user_id": user_id,
                    "field": field2,
                    "number": user_data[user_id][field2],
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


    if enter_calls=='3':
        user_id = input("Enter User ID: ")
        if user_id in user_data:
            print("choose (1, 2, or 3):", user_data[user_id])
            field1 = input("Enter field to print (or 'all' to print all fields): ")
            field2 = input("Enter field to print (or 'all' to print all fields): ")
            field3 = input("Enter field to print (or 'all' to print all fields): ") 
            if field1  in user_data[user_id]:
                add_time1=float(input("enter time:: "))
                add_time2=float(input("enter time:: "))
                add_time3=float(input("enter time:: "))
                Whatsappcall.phone_number(user_data[user_id][field1])
                Whatsappcall.timer(add_time1)
                add_timer2 = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print(f"{user_data[user_id][field1]} (Called at {add_timer2})")

            # Create a new dictionary to store timestamped data
                timestamped_data = {
                    "user_id": user_id,
                    "field": field1,
                    "number": user_data[user_id][field1],
                    "timestamp": add_timer2
                }
                with open('timestamped_data.json', 'a') as f:
                    json.dump(timestamped_data, f)
                    f.write('\n')  # Add a newline for readability
                sleep(1)
                send_keys("^%{VK_NUMPAD0}")
                sleep(3)
                Whatsappcall.phone_number(user_data[user_id][field2])
                Whatsappcall.timer(add_time2)
                add_timer3 = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print(f"{user_data[user_id][field2]} (Called at {add_timer3})")
                timestamped_data = {
                    "user_id": user_id,
                    "field": field2,
                    "number": user_data[user_id][field2],
                    "timestamp": add_timer3
                }
            # Write the timestamped data to a new file
                with open('timestamped_data.json', 'a') as f:
                    json.dump(timestamped_data, f)
                    f.write('\n')  # Add a newline for readability
                sleep(1)
                send_keys("^%{VK_NUMPAD0}")
                sleep(3)
                Whatsappcall.phone_number(user_data[user_id][field3])
                Whatsappcall.timer(add_time3)
                add_timer4 = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                print(f"{user_data[user_id][field3]} (Called at {add_timer4})")
                timestamped_data = {
                    "user_id": user_id,
                    "field": field2,
                    "number": user_data[user_id][field3],
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
def print_timestamped_data(user_id): 
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

while True:
    print("         -------------------------------------             ")
    print("             WELCOME TO PUZHAL PHONE PORTAL              ")
    print("           ----------------------------------             ")
    print("\n1. Store Data\n2. Make Call\n3. Search Data\n4. Quit")
    option = input("Enter your option: ")
    if option == '1':
        store_data()
    elif option == '2':
        retrieve_data()
    elif option == '3':
        user_id_input = input("Enter User ID to retrieve data: ")
        print_timestamped_data(user_id_input)
    elif option == '4':
        break
    else:
        print("Invalid option. Please try again.")
 
