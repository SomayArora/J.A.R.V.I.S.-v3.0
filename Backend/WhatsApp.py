import pywhatkit
import pyautogui
import re
import time
from Backend.TextToSpeech import TextToSpeech
from AppOpener import open as appopen

# Define contacts with numbers and aliases
contact_list = {
    "Mrs. Arora": {
        "numbers": ["+91 7838123873"],
        "aliases": ["mom", "mother", "maa"]
    },
    "Mr. Arora": {
        "numbers": ["+91 8076843976"],
        "aliases": ["dad", "father", "papa"]
    },
    "aditya": {
        "numbers": ["+91"
        "9800000000"],
        "aliases": ["Aditya", "Best friend"]
    },
    "sister": {
        "numbers": ["+919900000000"],
        "aliases": ["sister", "sis", "di"]
    }
}


# Find contact by spoken name
def find_contact(spoken_name):
    for key, info in contact_list.items():
        if spoken_name.lower() in info["aliases"]:
            return key, info["numbers"][0]  # (alias key, phone number)
    return None, None

# Search WhatsApp by number
def whatsapp_call(contact_number, contact_name, video=False):
    try:
        appopen("whatsapp")
        TextToSpeech(f"Calling {contact_name} via WhatsApp, Sir.")
        time.sleep(5)

        pyautogui.click(x=180, y=120)
        if contact_number == "+91 7838123873":
            pyautogui.typewrite("Mom")
            
        elif contact_number == "+91 8076843976":
            pyautogui.typewrite("Papa")
            
        else:  # Focus search bar (adjust)
            pyautogui.typewrite(contact_number)  # Search by number
        
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(1)

        if video:
            pyautogui.click(x=1793, y=68) # Video call button
        else:
            pyautogui.click(x=1845, y=68)  # Voice call button

    except Exception as e:
        TextToSpeech("Unable to complete the call, Sir.")
        print("Call error:", e)

# Main handler
def WhatsappHandler(command: str):
    command = command.lower()

    match = re.match(r"whatsapp\s+(message|call|video call)\s+(\w+)(.*)", command)
    if not match:
        TextToSpeech("I'm sorry Sir, I couldn't understand the WhatsApp command.")
        return

    action, spoken_name, message = match.groups()
    spoken_name = spoken_name.strip()
    message = message.strip()

    alias, number = find_contact(spoken_name)
    if not alias:
        TextToSpeech(f"I couldn't find {spoken_name} in your contacts, Sir.")
        return

    if action == "message":
        try:
            if not message:
                message = "Hello from Jarvis!"
            else:
                message = message.strip()
                message = message[0].upper() + message[1:] if message else message


            TextToSpeech(f"Sending message to {alias}, Sir.")
            pywhatkit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
            TextToSpeech(f"Message sent successfully to {alias}, Sir.")
        except Exception as e:
            TextToSpeech("Something went wrong while sending the message, Sir.")
            print("Messaging error:", e)

    elif action == "call":
        whatsapp_call(number, alias, video=False)

    elif action == "video call":
        whatsapp_call(number, alias, video=True)
