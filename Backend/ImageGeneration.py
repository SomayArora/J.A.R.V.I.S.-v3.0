import requests
from PIL import Image
from io import BytesIO
import os
from random import randint

import os
from dotenv import load_dotenv
load_dotenv()
HUGGINGFACE_API_KEY = os.environ.get("HuggingFaceAPIKey")
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

def GenerateImages(prompt, num_images=4, save_folder=r"D:\\J.A.R.V.I.S. v2.0\\Generated_Images"):

    os.makedirs(save_folder, exist_ok=True)

    for i in range(1, num_images + 1):
        payload = {
            "inputs": f"{prompt}, quality=4K, sharpness=maximum, ultra-detailed, high resolution, seed={randint(0, 1000000)}"
        }   
        response = requests.post(API_URL, headers=HEADERS, json=payload)

        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))

            filename = f"{prompt.replace(' ', '_')}_{i}.png"
            filepath = os.path.join(save_folder, filename)

            image.save(filepath)
            print(f"Image {i} saved at: {filepath}")
            image.show()

        else:
            print(f"Error {response.status_code}: {response.text}")



