from diffusers import StableDiffusionPipeline
import torch
import os
from datetime import datetime
import subprocess

def generate_images_fast(prompt, num_images=5, base_folder=r"D:\\J.A.R.V.I.S. v2.0\\Generated_Images"):
    # Create target folder
    folder_name = os.path.join(base_folder, prompt.replace(' ', '_'))
    os.makedirs(folder_name, exist_ok=True)

    print("Loading model...")
    pipe = StableDiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1", torch_dtype=torch.float16
    )
    pipe = pipe.to("cuda")

    print(f"Generating {num_images} images for: '{prompt}'")
    for i in range(1, num_images + 1):
        image = pipe(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]
        filename = f"{prompt.replace(' ', '_')}_{i}.png"
        filepath = os.path.join(folder_name, filename)
        image.save(filepath)
        print(f"Saved: {filepath}")

    # Open folder and launch first image in Photos
    try:
        os.startfile(folder_name)  # Opens File Explorer
        first_image = os.path.join(folder_name, os.listdir(folder_name)[0])
        subprocess.Popen(['explorer', first_image])
    except Exception as e:
        print(f"Could not open images: {e}")

generate_images_fast("RDJ as Doctor Doom")