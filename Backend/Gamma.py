from webbrowser import open as webopen
from Backend.TextToSpeech import TextToSpeech
import pyautogui
import time
import os
import shutil


DOWNLOADS_DIR = os.path.join(os.path.expanduser("~"), "Downloads")
DEST_DIR = "D:/J.A.R.V.I.S. v2.0/Generated_Presentations"

def wait_for_download(extension=".pdf", timeout=60):
    print("[*] Waiting for PDF to download...")
    elapsed = 0
    while elapsed < timeout:
        files = [f for f in os.listdir(DOWNLOADS_DIR) if f.endswith(extension)]
        if files:
            files = sorted(files, key=lambda x: os.path.getctime(os.path.join(DOWNLOADS_DIR, x)), reverse=True)
            file_path = os.path.join(DOWNLOADS_DIR, files[0])
            if not file_path.endswith(".crdownload"):  # Chrome download in progress
                print(f"[✓] Found file: {files[0]}")
                return file_path
        time.sleep(1)
        elapsed += 1
    print("[x] Download timed out.")
    return None

def move_file_to_destination(file_path):
    if not os.path.exists(DEST_DIR):
        os.makedirs(DEST_DIR)
    dest_path = os.path.join(DEST_DIR, os.path.basename(file_path))
    shutil.move(file_path, dest_path)
    print(f"[✓] Moved to: {dest_path}")
    TextToSpeech("Render is complete and ready for your review, Sir.")
    webopen(str(dest_path))  # Open the file after moving

def Presentation(topic):
    prompt = f"Create a presentation on the topic: {topic} by Somay Arora "
    TextToSpeech("Initiating presentation generation protocol, Sir.")
    print("[*] Opening Gamma...")
    webopen("https://gamma.app/create/generate")
    time.sleep(5)

    print("[*] Clicking input box...")
    pyautogui.click(x=666, y=462)
    time.sleep(1)

    print(f"[*] Typing topic: {topic}")
    pyautogui.typewrite(topic)
    time.sleep(1)
    pyautogui.press('enter')
    TextToSpeech("Commencing semantic analysis. Generating initial framework.")

    print("[*] Waiting for presentation to generate...")
    time.sleep(20)

    TextToSpeech("Framework generated. Proceeding to finalize presentation, Sir.")
    print("[*] Clicking Generate or Continue...")
    pyautogui.click(x=1116, y=992)
    time.sleep(30)

    TextToSpeech("Composition complete. Finalizing render for export.")
    print("[*] Clicking 3-dots menu...")
    pyautogui.click(x=1839, y=148)
    time.sleep(1)

    TextToSpeech("Export initiated. Transferring final asset to local storage.")
    print("[*] Clicking Download PDF (assumes it's at this position)...")
    pyautogui.click(x=1633, y=557)
    time.sleep(1)

    print("[*] Clicking Close button...")
    pyautogui.click(x=620, y=442)

    pdf_file = wait_for_download()
    if pdf_file:
        move_file_to_destination(pdf_file)

def Website(topic):
    TextToSpeech("Initiating website generation protocol, Sir.")
    print("[*] Opening Gamma...")
    webopen("https://gamma.app/create/generate")
    time.sleep(5)

    print("[*] Clicking Webpage box...")
    pyautogui.click(x=893, y=315)
    time.sleep(1)

    print("[*] Clicking input box...")
    pyautogui.click(x=666, y=462)
    time.sleep(1)

    print(f"[*] Typing topic: {topic}")
    pyautogui.typewrite(topic)
    time.sleep(1)
    pyautogui.press('enter')
    TextToSpeech("Commencing semantic analysis. Generating initial framework.")

    print("[*] Waiting for webpage to generate...")
    time.sleep(20)

    TextToSpeech("Framework generated. Proceeding to finalize presentation, Sir.")
    print("[*] Clicking Generate or Continue...")
    pyautogui.click(x=1116, y=992)
    time.sleep(30)

    TextToSpeech("Website composition complete. Finalizing render to publish.")
    print("[*] Clicking Publish")
    pyautogui.click(x=1697, y=142)
    time.sleep(15)

    print("[*] Clicking View Site...")
    pyautogui.click(x=1697, y=142)
    TextToSpeech("The final render is complete. Ready for your review, Sir.")





