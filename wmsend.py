import pandas as pd
import pywhatkit as kit
import pyautogui
import time
import platform
from screeninfo import get_monitors

monitor = get_monitors()[0]
screen_width = monitor.width
screen_height = monitor.height


# Read the CSV file
csv_file = "list.csv"
df = pd.read_csv(csv_file)


# Iterate through the rows and send messages
for index, row in df.iterrows():
    phone_number = row["phone_number"]
    message = row["message"]

    try:
        kit.sendwhatmsg_instantly(f"+{phone_number}", message, 10)
        pyautogui.moveTo(screen_width * 0.694, screen_height* 0.964) 
        pyautogui.click()
        pyautogui.press('enter') 
        print(f"Message sent to {phone_number}")
        time.sleep(3)
    except Exception as e:
        print(f"Error sending message to {phone_number}: {e}")

    # Wait for 3 seconds before sending the next message
    # Close the active browser tab
    if platform.system() == "Darwin":  # macOS
        pyautogui.hotkey("command", "w")
    else:  # Windows and Linux
        pyautogui.hotkey("ctrl", "w")
    pyautogui.press('enter') 
    time.sleep(3)


print("Finished sending messages.")
