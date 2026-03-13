
import random

greetings = ['hello', 'hi', 'hey', 'hola', 'hi there']
responses = ['hey', 'hi there', 'hello', 'hi', 'hola']

def generate_response(greeting):
    return random.choice(responses)

print("Chatbot: hi, I'm chatbot!")
while True:
    user_input = input("You: ").lower()
    if user_input in greetings:
        print("Chatbot:", generate_response(user_input))
    elif user_input == 'quit':
        break
    else:
        print("Chatbot: sorry, I didn't understand that!")
