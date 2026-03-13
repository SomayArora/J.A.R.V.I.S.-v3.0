from AppOpener import close, open as appopen  # Import functions to open and close apps.
from webbrowser import open as webopen  # Import web browser functionality-
from rich import print  # Import rich for styled console output.
from groq import Groq  # Import Groq for AI chat functionalities.
import webbrowser  # Import webbrowser for opening URLs.
import subprocess  # Import subprocess for interacting with the system.
import keyboard  # Import keyboard for keyboard-related actions.
import asyncio  # Import asyncio for asynchronous programming.
import os  # Imports os for operating system functionalities.
from Backend.TextToSpeech import TextToSpeech  # Import the TextToSpeech function from Backend/TextToSpeech.py.
import random  # Import random for generating random responses.
from serpapi import GoogleSearch
from datetime import datetime  # Import datetime for handling date and time.
import google.generativeai as genai
import pyautogui  # Import pyautogui for taking screenshots.
import speedtest
import pywhatkit
from pywinauto import Desktop
from io import BytesIO
import psutil
import socket
import speedtest
import sounddevice as sd
import soundcard as sc
import GPUtil  
import platform
import time


from dotenv import load_dotenv
load_dotenv()
GroqAPIKey = os.environ.get("GroqAPIKey")

# Define CSS classes for parsing specific elements in HTML content.
classes = ["LC20lb", "h3YkEe", "LTKOO SY7ric", "ZoL0C", "gsrt vk_bk FzWSb YwPhnf", "pclqee",
           "tw-Data-text tw-text-small tw-ta", "IZ6rdc", "OSR6d LTKOO", "vLzY6d",
           "webanswers-webanswers_table__webanswers-table", "dDoNo ikb4Bb gsrt", "sXLa0E",
           "LWkfKe", "VQF4gB", "qV3Wpe", "kno-rdesc", "SPZz6b"]

# Define a user-agent for making web requests.
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

# Initialize the Groq client with the API key.
client = Groq(api_key=GroqAPIKey)

# Predefined professional responses for user interactions.
professional_responses = [
    "Your satisfaction is my top priority; feel free to reach out if there's anything else I can help you with.",
    "I'm at your service for any additional questions or support you may need—don't hesitate to ask."
]

# List to store chatbot messages.
messages = []

# System message to provide context to the chatbot.
SystemChatBot = [{"role": "system", "content": f"Hello, I am {os.environ['Username']}, You're a content writer. You have to write content like lette"}]

play_song = [
    "Now playing your selected track, Sir.",
    "The requested song is now playing, Sir.",
    "Initiating playback as instructed, Sir.",
    "Your music selection is live, Sir.",
    "Commencing audio playback, Sir.",
    "The track is now streaming, Sir. Enjoy.",
    "Song playback has begun, Sir.",
    "Enjoy your music, Sir.",
    "Playback started as per your request, Sir.",
    "Your chosen song is now playing, Sir."
]

content_written = [
    "Your requested content has been prepared, Sir.",
    "Your document is ready, Sir.",
    "The content has been written and saved, Sir.",
    "I've finished composing your requested text, Sir.",
    "The content has been generated as per your instructions, Sir.",
    "I've successfully written the content, Sir.",
    "Your document is complete, Sir."
]

code_written = [
    "Your code has been generated as requested, Sir.",
    "I've written the code according to your instructions, Sir.",
    "The code is ready and available for your review, Sir.",
    "I've completed the coding task, Sir.",
    "Your program is now prepared, Sir.",
    "The requested script has been created, Sir.",
    "I've successfully written the code, Sir.",
    "Your coding request has been fulfilled, Sir."
]

google_search_responses = [
    "I've initiated a Google search for your query, Sir.",
    "Searching Google as requested, Sir.",
    "Your search results will be displayed shortly, Sir.",
    "I've started the Google search process, Sir.",
    "Retrieving information from Google now, Sir.",
    "Commencing Google search, Sir.",
    "Your requested information is being fetched from Google, Sir.",
    "Displaying Google search results, Sir.",
    "I've begun searching Google for your request, Sir.",
    "Google search underway, Sir."
]

youtube_search_responses = [
    "I've initiated a YouTube search for your query, Sir.",
    "Searching YouTube as requested, Sir.",
    "Your YouTube search results will be displayed shortly, Sir.",
    "I've started the YouTube search process, Sir.",
    "Retrieving videos from YouTube now, Sir.",
    "Commencing YouTube search, Sir.",
    "Your requested videos are being fetched from YouTube, Sir.",
    "Displaying YouTube search results, Sir.",
    "I've begun searching YouTube for your request, Sir.",
    "YouTube search underway, Sir."
]

open_app_responses = [
    "Launching the application, Sir.",
    "Opening as instructed, Sir.",
    "Starting the requested app now, Sir.",
    "Your application is now launching, Sir.",
    "Initiating the app for you, Sir.",
    "Executing your command to open the app, Sir.",
    "Accessing the program as per your request, Sir."
]

close_app_responses = [
    "Closing the application, Sir.",
    "I've shut down the requested app, Sir.",
    "The app has been terminated successfully, Sir.",
    "The program is now closed, Sir.",
    "Your instruction to close the app has been fulfilled, Sir.",
    "App closed as you commanded, Sir.",
    "That application is no longer running, Sir."
]

system_task_responses = [
    "Done, Sir.",
    "Command executed.",
    "Action completed, Sir.",
    "All set, Sir.",
    "It's taken care of.",
    "System task completed.",
    "As you wish, Sir.",
    "Processed the system command.",
    "That’s done.",
    "Finished executing the task, Sir."
]

known_websites = {
    "youtube": "www.youtube.com",
    "facebook": "www.facebook.com",
    "get hub": "www.github.com",
    "github": "www.github.com",
    "youtube studio": "studio.youtube.com",
    "twitter": "www.twitter.com",
    "instagram": "www.instagram.com",
    "linkedin": "www.linkedin.com",
    "wikipedia": "www.wikipedia.org",
    "reddit": "www.reddit.com",
    "pinterest": "www.pinterest.com",
    "quora": "www.quora.com",
    "tumblr": "www.tumblr.com",
    "flickr": "www.flickr.com",
    "snapchat": "www.snapchat.com",
    "tiktok": "www.tiktok.com",
    "vimeo": "www.vimeo.com",
    "dropbox": "www.dropbox.com",
    "onedrive": "www.onedrive.com",
    "google drive": "drive.google.com",
    "icloud": "www.icloud.com",
    "amazon": "www.amazon.com",
    "ebay": "www.ebay.com",
    "alibaba": "www.alibaba.com",
    "netflix": "www.netflix.com",
    "hulu": "www.hulu.com",
    "disney plus": "www.disneyplus.com",
    "hbo max": "www.hbomax.com",
    "spotify": "www.spotify.com",
    "soundcloud": "www.soundcloud.com",
    "apple music": "www.apple.com/apple-music",
    "pandora": "www.pandora.com",
    "deezer": "www.deezer.com",
    "bandcamp": "www.bandcamp.com",
    "bbc": "www.bbc.com",
    "cnn": "www.cnn.com",
    "nytimes": "www.nytimes.com",
    "the guardian": "www.theguardian.com",
    "forbes": "www.forbes.com",
    "bloomberg": "www.bloomberg.com",
    "reuters": "www.reuters.com",
    "espn": "www.espn.com",
    "fox news": "www.foxnews.com",
    "nbc news": "www.nbcnews.com",
    "cbs news": "www.cbsnews.com",
    "abc news": "www.abcnews.go.com",
    "msnbc": "www.msnbc.com",
    "npr": "www.npr.org",
    "wsj": "www.wsj.com",
    "yahoo news": "news.yahoo.com",
    "buzzfeed": "www.buzzfeed.com",
    "huffpost": "www.huffpost.com",
    "canva": "www.canva.com",
    "chatgpt": "chat.openai.com",
    "slack": "www.slack.com",
    "trello": "www.trello.com",
    "asana": "www.asana.com",
    "zoom": "www.zoom.us",
    "skype": "www.skype.com",
    "microsoft teams": "www.microsoft.com/microsoft-teams",
    "google meet": "meet.google.com",
    "webex": "www.webex.com",
    "jira": "www.atlassian.com/software/jira",
    "notion": "www.notion.so",
    "airtable": "www.airtable.com",
    "monday": "www.monday.com",
    "clickup": "www.clickup.com",
    "dropbox paper": "www.dropbox.com/paper",
    "confluence": "www.atlassian.com/software/confluence",
    "figma": "www.figma.com",
    "adobe xd": "www.adobe.com/products/xd.html",
    "invision": "www.invisionapp.com",
    "microsoft word": "www.microsoft.com/microsoft-365/word",
    "google docs": "docs.google.com",
    "medium": "www.medium.com",
    "wordpress": "www.wordpress.com",
    "wix": "www.wix.com",
    "squarespace": "www.squarespace.com",
    "shopify": "www.shopify.com",
    "bigcommerce": "www.bigcommerce.com",
    "weebly": "www.weebly.com",
    "godaddy": "www.godaddy.com",
    "namecheap": "www.namecheap.com",
    "bluehost": "www.bluehost.com",
    "siteground": "www.siteground.com",
    "hostgator": "www.hostgator.com",
    "dreamhost": "www.dreamhost.com",
    "a2 hosting": "www.a2hosting.com",
    "inmotion hosting": "www.inmotionhosting.com",
    "digitalocean": "www.digitalocean.com",
    "linode": "www.linode.com",
    "aws": "aws.amazon.com",
    "azure": "azure.microsoft.com",
    "google cloud": "cloud.google.com",
    "heroku": "www.heroku.com",
    "gitlab": "www.gitlab.com",
    "bitbucket": "bitbucket.org",
    "codepen": "codepen.io",
    "jsfiddle": "jsfiddle.net",
    "repl.it": "repl.it",
    "stack overflow": "stackoverflow.com",
    "stackoverflow careers": "stackoverflow.com/jobs",
    "glassdoor": "www.glassdoor.com",
    "indeed": "www.indeed.com",
    "linkedin jobs": "www.linkedin.com/jobs",
    "monster": "www.monster.com",
    "simplyhired": "www.simplyhired.com",
    "angel.co": "angel.co",
    "github jobs": "jobs.github.com",
    "ziprecruiter": "www.ziprecruiter.com",
    "careerbuilder": "www.careerbuilder.com",
    "snagajob": "www.snagajob.com",
    "dice": "www.dice.com",
    "jobs": "www.jobs.com",
    "bamboohr": "www.bamboohr.com",
    "workday": "www.workday.com",
    "adp": "www.adp.com",
    "sap successfactors": "www.sap.com/products/hcm.html",
    "oracle hcm": "www.oracle.com/applications/human-capital-management",
    "zenefits": "www.zenefits.com",
    "paycor": "www.paycor.com",
    "paycom": "www.paycom.com",
    "gusto": "www.gusto.com",
    "square": "squareup.com",
    "stripe": "www.stripe.com",
    "paypal": "www.paypal.com",
    "venmo": "www.venmo.com",
    "cash app": "cash.app",
    "robinhood": "www.robinhood.com",
    "etrade": "www.etrade.com",
    "fidelity": "www.fidelity.com",
    "charles schwab": "www.schwab.com",
    "vanguard": "investor.vanguard.com",
    "td ameritrade": "www.tdameritrade.com",
    "coinbase": "www.coinbase.com",
    "binance": "www.binance.com",
    "kraken": "www.kraken.com",
    "blockchain": "www.blockchain.com",
    "gemini": "www.gemini.com",
    "bitfinex": "www.bitfinex.com",
    "bitstamp": "www.bitstamp.net",
    "bittrex": "www.bittrex.com",
    "okex": "www.okex.com",
    "poloniex": "www.poloniex.com",
    "coindesk": "www.coindesk.com",
    "cointelegraph": "www.cointelegraph.com",
    "decrypt": "www.decrypt.co",
    "cryptoslate": "www.cryptoslate.com",
    "cryptonews": "www.cryptonews.com",
    "coinmarketcap": "www.coinmarketcap.com",
    "coingecko": "www.coingecko.com",
    "messari": "www.messari.io",
    "icodrops": "www.icodrops.com",
    "tokenmarket": "www.tokenmarket.net",
    "coinpaprika": "www.coinpaprika.com",
    "cryptocompare": "www.cryptocompare.com",
    "coincheckup": "www.coincheckup.com",
    "cryptobriefing": "www.cryptobriefing.com",
    "blockonomi": "www.blockonomi.com",
    "coininsider": "www.coininsider.com",
    "newsbtc": "www.newsbtc.com",
    "bitcoin.com": "www.bitcoin.com",
    "ethereum.org": "www.ethereum.org",
    "litecoin.com": "www.litecoin.com",
    "ripple.com": "www.ripple.com",
    "cardano.org": "www.cardano.org",
    "stellarlumens.com": "www.stellarlumens.com",
    "tezos.com": "www.tezos.com",
    "eos.io": "www.eos.io",
    "neo.org": "www.neo.org",
    "iota.org": "www.iota.org",
    "monero.org": "www.monero.org",
    "zcash.org": "www.zcash.org",
    "dash.org": "www.dash.org",
    "dogecoin.com": "www.dogecoin.com",
    "gpt":"www.chatgpt.com/",
    "fitgirl repacks": "www.fitgirl-repacks.site",
    "ova games": "www.ovagames.com"
}

# Function to perform a Google search.
def GoogleSearch(Topic):
    pywhatkit.search(Topic)  # Use pywhatkit's search function to perform a Google search.
    return True  # Indicate success.

def Content(Topic):
    # Nested function to open a file in Notepad.
    def OpenNotepad(File):
        default_text_editor = "notepad.exe"  # Default text editor.
        subprocess.Popen([default_text_editor, File])  # Open the file in Notepad.

    # Nested function to generate content using the AI chatbot.
    def ContentWriterAI(prompt):
        messages.append({"role": "user", "content": f"{prompt}"})  # Add the user's prompt to message history.

        completion = client.chat.completions.create(
            model="llama3-70b-8192",  # Specify the AI model.
            messages=SystemChatBot + messages,  # Include system instructions and chat history.
            max_tokens=2048,  # Limit the maximum tokens in the response.
            temperature=1,  # Adjust response randomness.
            top_p=1,  # Use nucleus sampling for response diversity.
            stream=True,  # Enable streaming response.
            stop=None  # Allow the model to determine stopping conditions.
        )

        Answer = ""  # Initialize an empty string for the response.

        # Process streamed response chunks.
        for chunk in completion:
            if chunk.choices[0].delta.content:  # Check for content in the current chunk.
                Answer += chunk.choices[0].delta.content  # Append the chunk to Answer.

        Answer = Answer.replace("</s>", "")  # Remove unwanted tokens from the response.
        messages.append({"role": "assistant", "content": Answer})  # Add the AI's response to message history.
        return Answer

    Topic: str = Topic.replace("Content ", "")  # Remove "Content" from the topic.
    ContentByAI = ContentWriterAI(Topic)  # Generate content using AI.

    # Save the generated content to a text file.
    with open(f"Data/{Topic.lower().replace(' ', '_')}.txt", "w", encoding="utf-8") as file:
        file.write(ContentByAI)  # Write the content to the file.
        file.close()

    OpenNotepad(f"Data/{Topic.lower().replace(' ', '_')}.txt")  # Open the file in Notepad.
    return True

def Code(query):
    # Infer file extension from query
    extension_map = {
        "python": ".py",
        "html": ".html",
        "css": ".css",
        "javascript": ".js",
        "js": ".js",
        "java": ".java",
        "c++": ".cpp",
        "c": ".c"
    }

    # Extract possible language keyword
    lang = next((lang for lang in extension_map if lang in query.lower()), "txt")
    ext = extension_map.get(lang, ".txt")

    filename = f"Data/{query.lower().replace(' ', '_')}{ext}"

    # AI prompt with instruction to only return code
    messages.append({"role": "user", "content": f"Write only code for this: {query} — no explanation, no comments, no conclusion, nothing, write only code"})

    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=SystemChatBot + messages,
        max_tokens=2048,
        temperature=1,
        top_p=1,
        stream=True,
        stop=None
    )

    answer = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            answer += chunk.choices[0].delta.content

    answer = answer.replace("</s>", "")
    answer = answer.replace("```", "")
    messages.append({"role": "assistant", "content": answer})

    with open(filename, "w", encoding="utf-8") as f:
        f.write(answer)

    try:
        subprocess.Popen([r"C:\Users\ADMIN\AppData\Local\Programs\PyCharm Community\bin\pycharm64.exe", filename])
# Try to open in VS Code
    except:
        subprocess.Popen(["notepad.exe", filename])  # Fallback to Notepad
    return True

def YouTubeSearch(Topic):
    UrlSearch = f"https://www.youtube.com/results?search_query={Topic}"
    webbrowser.open(UrlSearch)  # Open the search URL in a web browser.
    return True  # Indicate success.

def Play(query):
    query_lower = query.lower().strip()

    # Spotify playlist aliases
    spotify_playlists = {
        ("all time favorites", "my playlist", "my favorite playlist", "all time favorites playlist", "all time favorite", "all time favorite playlist"): "https://open.spotify.com/playlist/761HHHmSWBTmivLUWX8hiE?si=ce07d568e901487e",
        ("sad hours", "sad playlist", "sad hours playlist"): "https://open.spotify.com/playlist/3jSD0UTal15wAxcIB2qAwq?si=bcedc2abbfee4704",
        ("bhajan", "bhajan playlist"): "https://open.spotify.com/playlist/1a0NGg9Dg0mlV4r9i8xPUe?si=5639b6d10ab14b0b",
        ("sigma", "sigma playlist"): "https://open.spotify.com/playlist/1vq83kYb7nptVBSdKOIoum?si=9a939259cf294c63",
        ("air force", "air force playlist"): "https://open.spotify.com/playlist/2QqfCpRpG7VxY6KJuwC1EG?si=8bf0860e8e4d4c35",
        ("turkish", "turkish playlist"): "https://open.spotify.com/playlist/6Rq01YfYJlVGw1M8RUJUxP?si=ae7ff8124a2545dd",
        ("mummy", "mummy playlist"): "https://open.spotify.com/playlist/5hGU04OFTNXXvnLzUtueIF?si=7c1110db02a14fb2",
        ("phonks", "phonks playlist"): "https://open.spotify.com/playlist/2ybCjdtGz51PNkFlRwMGgJ?si=5b4b8691f04a4a02"
    }

    # Check for Spotify playlist aliases (strict match)
    for aliases, link in spotify_playlists.items():
        for alias in aliases:
            if alias == query_lower or alias in query_lower:
                print(f"Opening Spotify playlist: {alias}")
                webbrowser.open(link)
                time.sleep(4)
                pyautogui.click(x=485, y=423)  # simulate play click
                return True

    # Fallback to YouTube
    if "workshop music" in query:
        pywhatkit.playonyt("tony stark workshop music 1 hour")
        time.sleep(4)
        pyautogui.press("space")
    else:
        print(f"Playing on YouTube: {query}")
        pywhatkit.playonyt(query)
        return True

def OpenApp(app_name):
    """
    Opens desktop apps or known websites. Tries desktop app first, then known site, then guesses domain.
    """

    # Normalize
    spoken = app_name.lower().strip()
    cleaned = spoken.replace(" dot ", ".").replace(" dot", ".").replace("dot ", ".").strip()
    cleaned = cleaned.replace(" ", "")

    # ----------- 1. Try to open as a desktop app -----------
    try:
        if spoken == "get hub":
            spoken = "github"
        appopen(spoken, match_closest=True, output=True, throw_error=True)
        return True
    except:
        pass

    # ----------- 2. Check the known websites dictionary -----------
    for key, url in known_websites.items():
        if key in spoken or spoken in key:
            webbrowser.open(url)
            return True

    # ----------- 3. Try constructing a URL manually -----------
    for prefix in ["open ", "www.", "http://", "https://"]:
        if cleaned.startswith(prefix):
            cleaned = cleaned.replace(prefix, "", 1)

    if any(tld in cleaned for tld in [".com", ".org", ".net", ".in", ".xyz", ".ai", ".io", ".gov"]):
        url = cleaned if cleaned.startswith("http") else f"https://{cleaned}"
        webbrowser.open(url)
        return True

    try:
        guessed_url = f"https://www.{cleaned}.com"
        webbrowser.open(guessed_url)
        return True
    except:
        pass

    return False

# Function to close an application.
def CloseApp(app):
    if "chrome" in app:
        pass  # Skip if the app is Chrome.
    else:
        try:
            close(app, match_closest=True, output=True, throw_error=True)
            return True  # Indicate success.
        except:
            return False  # Indicate failure.

# Function to execute system-level commands.
def System(command):

    # Nested function to mute the system volume.
    def mute():
        keyboard.press_and_release("volume mute")
        keyboard.press_and_release("windows+ctrl+d")  # Simulate the mute key press.

    # Nested function to unmute the system volume.
    def unmute():
        keyboard.press_and_release("volume mute") 
        keyboard.press_and_release("windows+ctrl+f4") # Simulate the unmute key press.

    # Nested function to increase the system volume.
    def volume_up():
        keyboard.press_and_release("volume up")  # Simulate the volume up key press.

    # Nested function to decrease the system volume.
    def volume_down():
        keyboard.press_and_release("volume down")  # Simulate the volume down key press.

    def screenshot():

        try:
            # Create folder if it doesn't exist
            folder = r"C:\\Users\Somay Arora\\OneDrive\\Pictures\\Screenshots by J.A.R.V.I.S"
            if not os.path.exists(folder):
                os.makedirs(folder)

            # File name with timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            file_path = os.path.join(folder, f"Screenshot_{timestamp}.png")

            # Take and save screenshot
            image = pyautogui.screenshot()
            image.save(file_path)

            TextToSpeech("Screenshot taken, Sir.")

            print(f"✅ Screenshot saved at: {file_path}")
            return file_path
        except Exception as e:
            print("❌ Error taking screenshot:", e)

    def scroll(direction="down", amount=500):
        if direction.lower() == "down":
            pyautogui.scroll(-amount)
        elif direction.lower() == "up":
            pyautogui.scroll(amount)

    def CheckInternetSpeed():
        try:
            TextToSpeech("Initiating network diagnostics, Sir. Please hold.")
            st = speedtest.Speedtest()
            best = st.get_best_server()

            download_speed = round(st.download() / 1_000_000, 2)
            upload_speed = round(st.upload() / 1_000_000, 2)
            ping = round(best['latency'], 2)

            print(f"Download: {download_speed} Mbps | Upload: {upload_speed} Mbps")

            jarvis_line = (
                f"Sir, The network diagnostics is complete. "
                f"Download speed clocked at {download_speed} megabits per second. "
                f"Upload speed at {upload_speed} megabits per second. "
                f"Latency is {ping} milliseconds. "
                f"System is ready for any high-bandwidth operation, Sir."
            )

            TextToSpeech(jarvis_line)
            return download_speed, upload_speed

        except Exception as e:
            print("Error:", e)
            TextToSpeech("Sorry, I was unable to check the internet speed.")

    def get_visible_apps():
        """
        Returns a list of visible, user-opened application windows using pywinauto.
        """
        try:
            windows = Desktop(backend="uia").windows()
            visible_apps = []
            for win in windows:
                title = win.window_text()
                if title.strip() and not title.isspace():
                    visible_apps.append(title)
            return visible_apps
        except Exception as e:
            return [f"Error: {e}"]

    def check_running_app():
        TextToSpeech("Initiating system scan for active applications, Sir.")
        apps = get_visible_apps()

        if apps and not apps[0].startswith("Error"):
            print("Visible Applications:")
            for app in apps:
                print("•", app)
            names = ", ".join(apps[:6])
            TextToSpeech(f"Sir, I've completed the scan. Active foreground applications include:{names}.")
        else:
            print("No visible applications found.")
            TextToSpeech("I’m not detecting any active windows at the moment, Sir. Shall I open something for you?")

    def capture_screen():
        screenshot = pyautogui.screenshot()
        buffer = BytesIO()
        screenshot.save(buffer, format="PNG")
        return buffer.getvalue()

    def Check_Screen():
        image_bytes = capture_screen()

        genai.configure(api_key="AIzaSyAikjIVsGmL7Rge683RMLTEph56yvEMyWI")  # Replace this
        model = genai.GenerativeModel('gemini-1.5-flash')

        response = model.generate_content([
            "You are J.A.R.V.I.S., Tony Stark's AI. Professionally analyze this screen and describe what's going on in one sentence.",
            {"mime_type": "image/png", "data": image_bytes}
        ])

        text = response.text.strip()
        print(f"🧠 Gemini Analysis: {text}")
        TextToSpeech(f"Sir, here's the analysis: {text}")

    def System_Check():

        TextToSpeech("Running a full system diagnostic, Sir. Please hold.")

        # CPU Information and Usage
        try:
            cpu_name = platform.processor() or "Unknown CPU"
            cpu_usage = psutil.cpu_percent(interval=1)
            TextToSpeech(f"Processor: Intel i5 14400F")
            TextToSpeech(f"Current CPU usage is at {cpu_usage} percent.")
        except Exception:
            TextToSpeech("Unable to retrieve CPU information.")

        # GPU Information and Usage
        try:
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]
                TextToSpeech(f"Graphics card: NVIDIA GEFORCE RTX THIRTY SIXTY")
                TextToSpeech(f"Current GPU usage is at {gpu.load * 100:.0f} percent.")
            else:
                TextToSpeech("No dedicated GPU detected.")
        except Exception:
            TextToSpeech("Unable to retrieve GPU information.")

        # RAM Information and Usage
        try:
            ram_usage = psutil.virtual_memory().percent
            TextToSpeech(f"Installed memory: 16 gigabytes")
            TextToSpeech(f"Current RAM usage is at {ram_usage} percent.")
        except Exception:
            TextToSpeech("Unable to retrieve RAM information.")

        # Battery
        try:
            battery = psutil.sensors_battery()
            if battery:
                plugged = "charging" if battery.power_plugged else "not charging"
                TextToSpeech(f"Battery level is at {battery.percent} percent and it is {plugged}.")
            else:
                TextToSpeech("Battery not detected. Using a desktop system.")
        except Exception:
            TextToSpeech("Unable to access battery information.")

        # Internet Connection
        try:
            socket.create_connection(("8.8.8.8", 53), timeout=2)
            TextToSpeech("Internet connection is active.")
        except OSError:
            TextToSpeech("Internet connection is not available.")

        # Network Latency (Ping)
        try:
            st = speedtest.Speedtest()
            best = st.get_best_server()
            ping = int(best['latency'])
            TextToSpeech(f"Current network latency is approximately {ping} milliseconds.")
        except Exception:
            TextToSpeech("Unable to determine network latency.")

        # Microphone Check
        try:
            mic_names = [mic.name for mic in sc.all_microphones(include_loopback=False)]
            if mic_names:
                TextToSpeech(f"Microphone is available. Detected device: {mic_names[0]}")
            else:
                TextToSpeech("No microphone detected.")
        except Exception:
            TextToSpeech("Unable to access microphone information.")

        # Speaker Check
        try:
            speaker_names = [sp.name for sp in sc.all_speakers()]
            if speaker_names:
                TextToSpeech(f"Speaker output is functional. Detected device: {speaker_names[0]}")
            else:
                TextToSpeech("No speaker output device found.")
        except Exception:
            TextToSpeech("Unable to access speaker information.")

        TextToSpeech("System diagnostic complete, Sir. All systems are fully operational.")



    # Execute the appropriate command.
    if command == "mute":
        mute()

    elif command == "unmute":
        unmute()

    elif command == "volume up":
        volume_up()

    elif command == "volume down":
        volume_down()

    elif command == "check":
        System_Check()

    elif "screenshot" in command:
        screenshot()

    elif "scroll up" in command:
        scroll("up", 500)
        TextToSpeech("Scrolling up, Sir.")

    elif "scroll down" in command:
        scroll("down", 500)
        TextToSpeech("Scrolling down, Sir.")

    elif "internet" in command or "network" in command:
        CheckInternetSpeed()

    elif "apps" in command or "applications" in command:
        check_running_app()

    elif "check" in command and "screen" in command:
        Check_Screen()

    elif "scan" in command and "screen" in command:
        Check_Screen()

    return True  # Indicate success

async def TranslateAndExecute(commands: list[str]):
    funcs = []  # List to store asynchronous tasks.

    for command in commands:

        print("📦 Inside Automation block with command:", command)

        if command.startswith("open "):  # Handle "open" commands.
            if "open it" in command:  # Ignore "open it" commands.
                pass
            if "open file" == command:  # Ignore "open file" commands.
                pass
            else:
                fun = asyncio.to_thread(OpenApp, command.removeprefix("open "))  # Schedule app opening.
                funcs.append(fun)
                TextToSpeech(random.choice(open_app_responses))  # Announce the app opening with a random message.

        elif command.startswith("general "):  # Placeholder for general commands.
            pass

        elif command.startswith("realtime "):  # Placeholder for real-time commands.
            pass

        elif command.startswith("close "):  # Handle "close" commands.
            fun = asyncio.to_thread(CloseApp, command.removeprefix("close "))  # Schedule app closing.
            funcs.append(fun)
            TextToSpeech(random.choice(close_app_responses))  # Announce the app closing with a random message.

        elif command.startswith("play "):  # Handle "play" commands.
            fun = asyncio.to_thread(Play, command.removeprefix("play "))  # Schedule Youtube playback.
            funcs.append(fun)
            TextToSpeech(random.choice(play_song))  # Announce the playback with a random message.

        elif command.startswith("code "):
            fun = asyncio.to_thread(Code, command.removeprefix("code "))
            funcs.append(fun)
            TextToSpeech(random.choice(code_written))

        elif command.startswith("content code"):
            fun = asyncio.to_thread(Code, command.removeprefix("code "))
            funcs.append(fun)
            TextToSpeech(random.choice(code_written))

        elif command.startswith("content "):  # Handle "content" commands.
            fun = asyncio.to_thread(Content, command.removeprefix("content "))  # Schedule content creation.
            funcs.append(fun)
            TextToSpeech(random.choice(content_written))  # Announce content creation with a random message.

        elif command.startswith("google search "):  # Handle Google search commands.
            fun = asyncio.to_thread(GoogleSearch, command.removeprefix("google search "))  # Schedule Google search.
            funcs.append(fun)
            TextToSpeech(random.choice(google_search_responses))  # Announce the search with a random message.

        elif command.startswith("youtube search "):  # Handle Youtube search commands.
            fun = asyncio.to_thread(YouTubeSearch, command.removeprefix("youtube search "))  # Schedule Youtube search.
            funcs.append(fun)
            TextToSpeech(random.choice(youtube_search_responses))

        elif command.startswith("system "):  # Handle system commands.
            fun = asyncio.to_thread(System, command.removeprefix("system "))  # Schedule system command.
            funcs.append(fun)
            if command.removeprefix("system ") == "mute":
                pass
            elif "scroll" in command:
                pass
            elif "screenshot" in command:
                pass
            elif "internet" in command or "network" in command:
                pass
            elif "apps" in command or "applications" in command:
                pass
            elif "check" in command and "screen" in command:
                pass
            elif "scan" in command and "screen" in command:
                pass
            elif "system check" in command:
                pass
            else:
                TextToSpeech(random.choice(system_task_responses))            
        else:
            print(f"No Function Found. For {command}")

    results = await asyncio.gather(*funcs)  # Execute all tasks concurrently.

    for result in results:  # Process the results.
        if isinstance(result, str):
            yield result
        else:
            yield result

# Asynchronous function to automate command execution.
async def Automation(commands: list[str]):

    async for result in TranslateAndExecute(commands): # Translate
        pass

    return True  # Indicate success.


