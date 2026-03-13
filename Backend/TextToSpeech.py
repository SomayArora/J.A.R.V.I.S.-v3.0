import os
import requests
import threading
import random
import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment
import re
import time

# Predefined Jarvis-style responses
responses = [
    "I've compiled the remainder of the data for your review Sir.",
    "The rest of the information is now available on your display Sir.",
    "I've processed the remaining details and logged them for you Sir.",
    "The additional data has been stored for later reference Sir.",
    "You’ll find the remaining specifications in your system logs Sir.",
    "I have archived the extended information for future access Sir.",
    "Displaying the remaining details on your console now Sir.",
    "I've prioritized the most relevant details for verbal transmission Sir.",
    "For efficiency, I have summarized the key points Sir.",
    "The extended data set has been transferred to your mainframe Sir.",
    "Shall I proceed with a full system report instead, Sir?",
    "I've filtered out the unnecessary details for brevity Sir.",
    "Compiling the remaining dataset into a report for later access Sir.",
    "Would you like me to highlight only the critical elements, Sir?",
    "I've streamlined the information for clarity Sir.",
    "Retrieving the remaining data upon your request Sir.",
    "For convenience, I've logged the extended details in your database Sir.",
    "Shall I summarize the remaining data further, Sir?",
    "I've omitted redundant information for efficiency Sir.",
    "Would you prefer a more detailed breakdown, Sir?"
]


def generate_audio(message: str, voice: str = "Matthew") -> str:
    """Fetches TTS audio from StreamElements API and saves it as an MP3 file."""
    url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={message}"

    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            mp3_path = "temp_voice.mp3"
            with open(mp3_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)  # Write in chunks to reduce delay
            return convert_to_wav(mp3_path)  # Convert to WAV
        else:
            print(f"❌ Error: API returned status {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"❌ Network error: {e}")
        return None


def convert_to_wav(mp3_path):
    """Converts MP3 to WAV for better playback compatibility."""
    wav_path = mp3_path.replace(".mp3", ".wav")
    sound = AudioSegment.from_mp3(mp3_path)
    sound.export(wav_path, format="wav", bitrate="192k")
    os.remove(mp3_path)
    return wav_path

def Co_speak(audio_file):
    """Plays the WAV file using sounddevice and blocks until done."""
    if not os.path.exists(audio_file):
        print(f"❌ Error: File {audio_file} not found.")
        return

    try:
        data, samplerate = sf.read(audio_file, dtype='float32')
        duration = len(data) / samplerate

        # Force full blocking play
        sd.play(data, samplerate)
        time.sleep(duration + 0.5)  # Wait for duration + buffer

        os.remove(audio_file)

    except Exception as e:
        print(f"❌ Playback error: {e}")

def TextToSpeech(text: str):
    """Processes and plays the given text as speech."""
    if not text:
        return

    # Improved sentence splitting
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentence_limit = 6 if len(sentences) >= 6 else len(sentences)

    if len(sentences) > 6 or len(text) > 200:
        trimmed_text = " ".join(sentences[:sentence_limit]).strip()
        if not trimmed_text.endswith((".", "!", "?")):
            trimmed_text += "."
        response = random.choice(responses)
        trimmed_audio = generate_audio(trimmed_text)
        if trimmed_audio:
            Co_speak(trimmed_audio)
        response_audio = generate_audio(response)
        if response_audio:
            Co_speak(response_audio)
    else:
        audio_file = generate_audio(text)
        if audio_file:
            Co_speak(audio_file)

TextToSpeech("Welcome back, Sir!")  # Initial greeting
#TextToSpeech("Welcome back, Sir! I've been monitoring the suit's systems during your absence. All functions are nominal, and the armor is ready for further deployment. How may I assist you now, Sir ?")
