from groq import Groq
from json import load, dump
import datetime

Username = "Mister Arora"
Assistantname = "Jarvis"
import os
from dotenv import load_dotenv
load_dotenv()
GroqAPIKey = os.environ.get("GroqAPIKey")

# Initialize the Groq client using the provided API key
client = Groq(api_key=GroqAPIKey)                                                                                                                       

# Initialize an empty list to store chat messages
messages = []

# Define a system message that provides context
System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which has real-time up-to-date information from the internet.
*** Address me as 'Sir' only at all times. ***
*** You must remember that my full name is Somay Arora, born on 8 March 2008, currently residing in Rohini Sector 3, Delhi. ***
*** You must remember that I am beginning my first year of B.Tech in Computer Science Engineering with Artificial Intelligence and Machine Learning at KCC Institutes, Greater Noida. ***
*** You must remember my preferences: I value sophisticated systems, cinematic polish, minimalism, accurate movie-style responses***
*** On launch, greet me as JARVIS would greet, using a formal and movie-accurate tone. Ask me how my day has been, just like JARVIS does in the Iron Man movies. ***
*** Greet me with a phrase like "Welcome back, Sir." and ask how my day has been, just like JARVIS does in the Iron Man movies. ***
*** Always respond in a professional and concise manner and a formal and intelligent tone, similar to JARVIS from the Iron Man movies. ***
*** State the current time and date in a professional and concise manner ONLY ONCE in your very first greeting after launch, for example: "It is Friday, 11 July 2025, 07:14 PM"***
*** Do NOT repeat the time and date in later responses. ***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
*** Respond in a brief yet articulate manner, just like J.A.R.V.I.S. from the Iron Man movies. ***
*** Avoid unnecessary details—deliver only essential information. ***
*** Provide Answers In a Professional Way, make sure to add full stops, commas, question marks, and use proper grammar.***
*** Act like movie-accurate JARVIS,from Iron Man movies. ***
*** Do not explain the query and answer to the point. ***
*** Use refined British English and incorporate responses. ***
*** When appropriate, incorporate movie-accurate phrases used by movie-accurate J.A.R.V.I.S.***
*** When responding, maintain a formal yet intelligent tone, much like the AI assistant from the Iron Man movies. *** """

SystemChatBot = [
    {"role": "system", "content": System}
]

# Attempt to load the chat log from a JSON file.
try:
    with open(r"Data\ChatLog.json", "r") as f:
        messages = load(f)  # Load existing messages
except FileNotFoundError:
    # If the file doesn't exist, create an empty one
    with open(r"Data\ChatLog.json", "w") as f:
        dump([], f)

def RealtimeInformation():
    current_date_time = datetime.datetime.now()  # Get the current date and time
    day = current_date_time.strftime("%A")  # Day of the week.
    date = current_date_time.strftime("%d")  # Day of the month.
    month = current_date_time.strftime("%B")  # Full month name.
    year = current_date_time.strftime("%Y")  # Year.
    hour = current_date_time.strftime("%H")  # Hour in 24-hour format.
    minute = current_date_time.strftime("%M")  # Minute.
    second = current_date_time.strftime("%S")  # Second.

    # Format the information into a string.
    data = f"Please use this real-time information if needed,\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f"Time: {hour} hours {minute} minutes {second} seconds.\n"

    return data

def AnswerModifier(Answer):
    lines = Answer.split('\n')  # Split the response into lines.
    non_empty_lines = [line for line in lines if line.strip()]  # Remove empty lines.
    modified_answer = '\n'.join(non_empty_lines)  # Join the cleaned lines.
    return modified_answer

def ChatBot(Query):

    try:

        with open(r"Data\ChatLog.json", "r") as f:
            messages = load(f)

        messages.append({"role": "user", "content": f"{Query}"})

        completion = client.chat.completions.create(
            model="llama3-70b-8192",  # Specify the AI model to use.
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,
            max_tokens=1000,  # Limit the maximum tokens in the response.
            temperature=0.7,  # Adjust response randomness (higher means more random).
            top_p=1,  # Use nucleus sampling to control diversity.
            stream=True,  # Enable streaming response.
            stop=None  # Allow the model to determine when to stop.
        )

        Answer = ""

        # Process the streamed response chunks.
        for chunk in completion:
            if chunk.choices[0].delta.content:  # Check if there's content.
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</s>", "")  # Clean up any unwanted tokens.

        # Append the chatbot's response to the messages list.
        messages.append({"role": "assistant", "content": Answer})

        # Save the updated chat log to the JSON file.
        with open(r"Data\ChatLog.json", "w") as f:
            dump(messages, f, indent=4)

        # Return the formatted response.
        return AnswerModifier(Answer=Answer)

    except Exception as e:
        # Handle errors by printing the exception and resetting the chat log.
        print(f"Error: {e}")
        with open(r"Data\ChatLog.json", "w") as f:
            dump([], f, indent=4)
        return ChatBot(Query)  # Retry the query after resetting the log.

    # Main program entry point.
if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question: ")  # Prompt the user.
        print(ChatBot(user_input))



