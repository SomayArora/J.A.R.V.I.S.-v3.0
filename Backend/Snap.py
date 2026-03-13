import sounddevice as sd
import numpy as np
import time
import pyautogui
from Backend.TextToSpeech import TextToSpeech

# Config
SAMPLE_RATE = 44100
BLOCK_DURATION = 0.3  # in seconds
COOLDOWN = 1
TIMEOUT_AFTER_LAST_SNAP = 5

LOW_FREQ = 300
HIGH_FREQ = 1300
FREQ_THRESHOLD = 14  # Adjust this based on your tests

ENERGY_THRESHOLD = 0.15  # You may need to adjust this value

def Snap(task):
    TextToSpeech("Sure Sir")
    print("🎧 Snap detection (energy-based) started.")
    last_snap_time = None
    first_snap_detected = False
    last_detection_time = time.time()

    def callback(indata, frames, time_info, status):
        nonlocal last_snap_time, first_snap_detected, last_detection_time
        audio = indata[:, 0]
        rms_energy = np.sqrt(np.mean(audio**2))

        current_time = time.time()
        if rms_energy > ENERGY_THRESHOLD:
            if not first_snap_detected or (current_time - last_snap_time > COOLDOWN):
                print(f"✨ Snap/Clap detected (RMS energy: {rms_energy:.3f})")
                if "apps" in task or "app" in task:
                    pyautogui.hotkey('alt', 'tab')
                else:    
                    pyautogui.press('right')
                last_snap_time = current_time
                last_detection_time = current_time
                first_snap_detected = True

    with sd.InputStream(callback=callback, channels=1, samplerate=SAMPLE_RATE, blocksize=int(SAMPLE_RATE * BLOCK_DURATION)):
        while True:
            sd.sleep(int(BLOCK_DURATION * 1000))
            if first_snap_detected and (time.time() - last_detection_time >= TIMEOUT_AFTER_LAST_SNAP):
                print("⏹️ No snap for 5 seconds. Exiting.")
                break