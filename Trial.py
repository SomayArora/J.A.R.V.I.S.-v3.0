import requests
import base64
from PIL import Image
from io import BytesIO
import os
from random import randint

# Set your API key directly
import os
from dotenv import load_dotenv
load_dotenv()
HUGGINGFACE_API_KEY = os.environ.get("HuggingFaceAPIKey")  # Replace with your actual API key
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}


def GenerateImages(prompt, num_images=4, save_folder="Generated_Images"):
    """Generates multiple images from a prompt using Hugging Face's API and saves them locally."""

    # Create folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    for i in range(1, num_images + 1):
        payload = {
            "inputs": f"{prompt}, quality=4K, ultra-detailed, seed={randint(0, 1000000)}"
        }
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            # Open the image from response
            image = Image.open(BytesIO(response.content))

            # Generate a unique filename
            filename = f"{prompt.replace(' ', '_')}_{i}.png"
            filepath = os.path.join(save_folder, filename)

            # Save and show the image
            image.save(filepath)
            print(f"Image {i} saved at: {filepath}")
            image.show()

        else:
            print(f"Error {response.status_code}: {response.text}")

