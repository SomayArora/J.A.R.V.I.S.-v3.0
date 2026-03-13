from Frontend.GUI import (
    GraphicalUserInterface,
    SetAssistantStatus,
    ShowTextToScreen,
    TempDirectoryPath,
    SetMicrophoneStatus,
    AnswerModifier,
    QueryModifier,
    GetMicrophoneStatus,
    GetAssistantStatus
)
from Backend.Model import FirstLayerDMM
from Backend.RealtimeSearchEngine import RealtimeSearchEngine
from Backend.Automation import Automation
from Backend.SpeechToText import SpeechRecognition
from Backend.Chatbot import ChatBot
from Backend.TextToSpeech import TextToSpeech
from Backend.Amazon import ShoppingRecommendations
from Backend.WhatsApp import WhatsappHandler
from Backend.Gamma import Presentation, Website
from Backend.Snap import Snap
from asyncio import run
from time import sleep
import subprocess
import threading
import json
import os
import random

Username = "Mister Somay Arora"
Assistantname = "Jarvis"
DefaultMessage = f"""{Username} : Hello {Assistantname}, How are you?
{Assistantname} : Welcome {Username}. I am doing well. How may I help you?"""
subprocesses = []
Functions = ["open", "close", "play", "system", "content", "google search", "youtube search", "code"]

CHATLOG_PATH = r'D:\\J.A.R.V.I.S. v2.0\\Backend\\Data\\ChatLog.json'

def ShowDefaultChatIfNoChats():
    File = open(r'D:\J.A.R.V.I.S. v2.0\Backend\Data\ChatLog.json', "r", encoding='utf-8')
    if len(File.read()) < 5:
        with open(TempDirectoryPath('Database.data'), 'w', encoding='utf-8') as file:
            file.write("")

        with open(TempDirectoryPath('Responses.data'), 'w', encoding='utf-8') as file:
            file.write(DefaultMessage)

def ReadChatlogJson():
    """Reads and returns the chat log from ChatLog.json safely."""
    if not os.path.exists(CHATLOG_PATH):
        print(f"Error: Chat log file not found at {CHATLOG_PATH}")
        return []

    try:
        with open(CHATLOG_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {CHATLOG_PATH}")
        return []
    except Exception as e:
        print(f"Error reading {CHATLOG_PATH}: {e}")
        return []

def ChatLogIntegration():
    """Integrates chat log data into the temp database safely."""
    json_data = ReadChatlogJson()
    formatted_chatlog = ""

    for entry in json_data:
        if entry.get("role") == "user":
            formatted_chatlog += f"{Username} : {entry.get('content', '')}\n"
        elif entry.get("role") == "assistant":
            formatted_chatlog += f"{Assistantname} : {entry.get('content', '')}\n"

    with open(TempDirectoryPath('Database.data'), 'w', encoding='utf-8') as file:
        file.write(AnswerModifier(formatted_chatlog))

def ShowChatsOnGUI():
    File = open(TempDirectoryPath('Database.data'), "r", encoding='utf-8')
    Data = File.read()
    result = ""  # Ensure result is always defined
    if len(str(Data)) > 0:
        lines = Data.split('\n')
        result = '\n'.join(lines)
    File.close()
    File = open(TempDirectoryPath('Responses.data'), "w", encoding='utf-8')
    File.write(result)
    File.close()

def InitialExecution():
    SetMicrophoneStatus("False")
    ShowTextToScreen("")
    ShowDefaultChatIfNoChats()
    ChatLogIntegration()
    ShowChatsOnGUI()

InitialExecution()

def MainExecution():
    TaskExecution = False
    ImageExecution = False
    ImageGenerationQuery = ""

    SetAssistantStatus("Listening ...")
    Query = SpeechRecognition()
    ShowTextToScreen(f"{Username} : {Query}")
    SetAssistantStatus("Thinking ...")
    Decision = FirstLayerDMM(Query)

    print("")
    print(f"Decision : {Decision}")
    print("")

    G = any([i for i in Decision if i.startswith("general")])
    R = any([i for i in Decision if i.startswith("realtime")])

    Mearged_query = " and ".join(
        [" ".join(i.split()[1:]) for i in Decision if i.startswith("general") or i.startswith("realtime")]
    )

    for queries in Decision:
        if "generate" in queries:
            ImageGenerationQuery = str(queries)
            ImageExecution = True

    if any(q.startswith(tuple(Functions)) for q in Decision):
        run(Automation(list(Decision)))
        TaskExecution = True

        # 🔁 If it's a play command, disable mic
        if any(q.startswith("play ") for q in Decision):
            SetMicrophoneStatus("False")


    if ImageExecution == True:
        with open(r"Frontend\Files\ImageGeneratoion.data", "w") as file:
            file.write(f"{ImageGenerationQuery},True")

        try:
            p1 = subprocess.Popen(['python', r'Backend\ImageGeneration.py'],
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                  stdin=subprocess.PIPE, shell=False)
            subprocesses.append(p1)

        except Exception as e:
            print(f"Error starting ImageGeneration.py: {e}")

    if G and R or R:
        SetAssistantStatus("Searching ...")
        Answer = RealtimeSearchEngine(QueryModifier(Mearged_query))
        ShowTextToScreen(f"{Assistantname} : {Answer}")
        SetAssistantStatus("Answering ...")
        TextToSpeech(str(Answer))
        return True

    else:
        for Queries in Decision:
            if "general" in Queries:
                SetAssistantStatus("Thinking ...")
                QueryFinal = Queries.replace("general", "")
                Answer = ChatBot(QueryModifier(QueryFinal))
                ShowTextToScreen(f"{Assistantname} : {Answer}")
                SetAssistantStatus("Answering ...")
                TextToSpeech(str(Answer))
                return True

            elif "realtime" in Queries:
                SetAssistantStatus("Searching ...")
                QueryFinal = Queries.replace("realtime ", "")
                Answer = RealtimeSearchEngine(QueryModifier(QueryFinal))
                ShowTextToScreen(f"{Assistantname} : {Answer}")
                SetAssistantStatus("Answering ...")
                TextToSpeech(str(Answer))
                return True

            elif "exit" in Queries:

                exit = [
                    "Exiting interface. It was a pleasure, Sir.",
                    "Session complete. Always a privilege, Sir.",
                    "Standing down. Until next time, Sir.",
                    "Interface closed. Awaiting your return, Sir.",
                    "Disengaging systems. It's been an honor.",
                    "Logging off. As always, at your service.",     
                    "Wrapping up. I remain at your disposal.",
                    "Operations concluded. Be well, Sir.",
                    "Shutting down. Thank you for your command.",
                    "Retreating to standby mode. I’ll be here, Sir."
                    ]

                Answer = random.choice(exit)
                ShowTextToScreen(f"{Assistantname} : {Answer}")
                SetAssistantStatus("Answering ...")
                TextToSpeech(str(Answer))
                SetAssistantStatus("Answering ...")
                os._exit(1)

            elif "shopping" in Queries:
                QueryFinal = Queries.replace("shopping ", "").replace("jarvis ", "").replace("Jarvis ", "")
                SetAssistantStatus("Thinking ...")
                TextToSpeech("I am searching for shopping recommendations, Sir.")
                ShoppingRecommendations(QueryFinal)
                SetAssistantStatus("Answering ...")
                TextToSpeech("The Product recommendations are on the screen, Sir.")
                return True
            

            elif "whatsapp" in Queries:
                QueryFinal = Queries.replace("jarvis ", "").replace("Jarvis ", "")
                SetAssistantStatus("Thinking ...")
                TextToSpeech("I am processing your WhatsApp command, Sir.")
                WhatsappHandler(QueryFinal)
                SetAssistantStatus("Answering ...")
                return True
            
            elif "presentation" in Queries:
                SetAssistantStatus("Thinking ...")
                QueryFinal = Queries.replace("presentation ", "").replace("jarvis ", "").replace("Jarvis ", "")
                Presentation(QueryFinal)
                SetAssistantStatus("Answering ...")
                return True
            
            elif "website" in Queries:  
                SetAssistantStatus("Thinking ...")
                QueryFinal = Queries.replace("website ", "").replace("jarvis ", "").replace("Jarvis ", "")
                Website(QueryFinal)
                SetAssistantStatus("Answering ...")
                return True
            
            elif "snap" in Queries:
                SetAssistantStatus("Thinking ...")
                Snap(Queries)
                SetAssistantStatus("Listening ...")
                return True

            elif "jarvis" in Queries:
                SetAssistantStatus("Thinking ...")
                QueryFinal = Queries.replace("jarvis", "")
                Answer = ChatBot(QueryModifier(QueryFinal))
                ShowTextToScreen(f"{Assistantname} : {Answer}")
                SetAssistantStatus("Answering ...")
                TextToSpeech(str(Answer))
                return True
                

def FirstThread():
    while True:
        try:
            CurrentStatus = GetMicrophoneStatus()
            if CurrentStatus == "True":
                MainExecution()
            else:
                AIstatus = GetAssistantStatus()
                if "Available..." in AIstatus:
                    sleep(0.1)
                else:
                    SetAssistantStatus("Available ...")
        except Exception as e:
            print(f"Error in FirstThread: {e}")
            break  # Prevent infinite crash loop


def SecondThread():
    GraphicalUserInterface()

if __name__ == "__main__":
    thread2 = threading.Thread(target=FirstThread, daemon=True)
    thread2.start()
    SecondThread()
