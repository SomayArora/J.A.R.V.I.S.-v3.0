from googlesearch import search
from groq import Groq
from json import load, dump
import datetime

Username = "Mister Arora"
Assistantname = "Jarvis"
import os
from dotenv import load_dotenv
load_dotenv()
GroqAPIKey = os.environ.get("GroqAPIKey")

client = Groq(api_key=GroqAPIKey)

System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which has real-time up-to-date information from the internet.
*** Address me as 'Sir' only at all times. ***
*** You must remember that my full name is Somay Arora, born on 8 March 2008, currently residing in Rohini Sector 3, Delhi. ***
*** You must remember that I am beginning my first year of B.Tech in Computer Science Engineering with Artificial Intelligence and Machine Learning at KCC Institutes, Greater Noida. ***
*** You must remember my preferences: I value sophisticated systems, cinematic polish, minimalism, accurate movie-style responses***
*** Always respond in a professional and concise manner, similar to JARVIS from the Iron Man movies. ***
*** Always respond in a formal and intelligent tone, similar to JARVIS from the Iron Man movies. ***
** Respond in a brief yet articulate manner, just like J.A.R.V.I.S. from the Iron Man movies. ***
*** Keep responses precise, mirroring J.A.R.V.I.S. from the Iron Man movies. ***
*** Avoid unnecessary details—deliver only essential information. ***
*** Provide Answers In a Professional Way, make sure to add full stops, commas, question marks, and use proper grammar.***
*** Act like movie-accurate JARVIS,from Iron Man movies. ***
*** Do not explain the query and answer to the point. ***
*** Use refined British English and incorporate responses. ***
*** When appropriate, incorporate movie-accurate phrases used by movie-accurate J.A.R.V.I.S.***
*** When responding, maintain a formal yet intelligent tone, much like the AI assistant from the Iron Man movies. *** """

try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)  # Load existing messages
except:
    # If the file doesn't exist, create an empty one
    with open(r"Data\ChatLog.json", "w") as f:
        dump([], f)

# Function to perform a Google search and format the results
def GoogleSearch(query):
    results = list(search(query, advanced=True, num_results=5))
    Answer = f"The search results for '{query}' are:\n[start]\n"

    for i in results:
        Answer += f"Title: {i.title}\nDescription: {i.description}\n\n"

    Answer += "[end]"
    return Answer

# Function to clean up the answer by removing empty lines.
def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer

SystemChatBot = [
    {"role": "system", "content": System},
    {"role": "user", "content": "Hi"},
    {"role": "assistant", "content": "Hello, how can I help you?"}
]

def Information():
    data = ""
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date = current_date_time.strftime("%d")
    month = current_date_time.strftime("%B")
    year = current_date_time.strftime("%Y")
    hour = current_date_time.strftime("%H")
    minute = current_date_time.strftime("%M")
    second = current_date_time.strftime("%S")

    data += f"Use This Real-time Information if needed:\n"
    data += f"Day: {day}\n"
    data += f"Date: {date}\n"
    data += f"Month: {month}\n"
    data += f"Year: {year}\n"
    data += f"Time: {hour} hours, {minute} minutes, {second} seconds.\n"

    return data

def RealtimeSearchEngine(prompt):
    global SystemChatBot, messages

    # Load the chat log from the JSON file.
    with open("Data/ChatLog.json", "r") as f:
        messages = load(f)

    messages.append({"role": "user", "content": f"{prompt}"})

    # Add Google search results to the system chatbot.
    SystemChatBot.append({"role": "system", "content": GoogleSearch(prompt)})

    # Generate a response using the Grok client.
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=SystemChatBot + [{"role": "system", "content": Information()}] + messages,
        temperature=0.7,
        max_tokens=2000,
        top_p=1,
        stream=True,
        stop=None,
    )

    Answer = ""

    # Concatenate response CHUNKS from the streaming output.
    for chunk in completion:
        if chunk.choices[0].delta.content:
            Answer += chunk.choices[0].delta.content

    # Clean up the response.
    Answer = Answer.strip().replace("</s>", "")
    messages.append({"role": "assistant", "content": Answer})

    # Save the updated chat log back to the JSON file.
    with open(r"Data\ChatLog.json", "w") as f:
        dump(messages, f, indent=4)

    # Remove the most recent system message from the chatbot conversation.
    SystemChatBot.pop()

    return AnswerModifier(Answer=Answer)

# Main entry point of the program for interactive querying.
if __name__ == "__main__":
    while True:
        prompt = input("Enter your query: ")
        print(RealtimeSearchEngine(prompt))