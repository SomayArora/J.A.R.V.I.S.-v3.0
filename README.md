# J.A.R.V.I.S. v3.0

An advanced, highly capable AI assistant inspired by Tony Stark's J.A.R.V.I.S., designed to automate tasks, provide real-time information, and assist with daily computing activities.

## Features

* **Conversational Chatbot**: Powered by advanced LLMs via Groq for intelligent, context-aware conversations.
* **Real-time Search Engine**: Fetches and processes up-to-date information from the web.
* **System Automation**: Controls system volume, takes screenshots, checks internet speed, and hardware diagnostics via python libraries.
* **Application Control**: Opens and closes desktop applications and websites seamlessly.
* **Content Generation**: Capable of writing code, stories, and generating text dynamically.
* **Image Generation**: Generates high-quality images via Hugging Face API (Stable Diffusion XL).
* **Media Playback**: Plays music directly from Spotify playlists or YouTube.
* **WhatsApp Automation**: Send messages and make calls via PyWhatKit.

## Prerequisites

- Python 3.10+
- [Groq API Key](https://console.groq.com)
- [Hugging Face API Key](https://huggingface.co)
- [Cohere API Key](https://dashboard.cohere.com/)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/SomayArora/J.A.R.V.I.S.-v3.0.git
   cd J.A.R.V.I.S.-v3.0
   ```

2. **Install dependencies:**
   ```bash
   pip install -r Requirements.txt
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API keys:
   ```env
   CohereAPIKey=your_cohere_api_key
   GroqAPIKey=your_groq_api_key
   HuggingFaceAPIKey=your_hugging_face_api_key
   Username=Your Name
   Assistantname=Jarvis
   ```

## Usage

Run the main file to start J.A.R.V.I.S.:

```bash
python Main.py
```

## Built With

- [Groq](https://groq.com/) - High-speed LLM inference
- [Hugging Face](https://huggingface.co/) - Image Generation
- [Cohere](https://cohere.com/) - Command generation and context understanding
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) & [Keyboard](https://github.com/boppreh/keyboard) - Automation
