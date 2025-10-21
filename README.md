# Flask Whisper Audio Transcription App

This project is a simple Flask web application that uses OpenAI's Whisper model to transcribe audio files (WAV format) to text **with timestamps**. It is intended for Windows systems but can be adapted to other platforms.

---

## Features

- Transcribes audio to text using Whisper
- Displays segment-level timestamps
- Simple Flask-based web UI
- Downloadable audio file endpoint

---

## Prerequisites

- **Python 3.10 or 3.11** (recommended)  
  *Note:* Some issues possible with Python 3.13+
- **ffmpeg** installed and accessible in your system PATH
- `Recording.wav` sample present in project directory

---

## Setup Instructions

### 1. Clone the repository

git clone https://github.com/PSAbhinav/audio-text-flask-app.git
cd audio-text-flask-app

### 2. Create a Python virtual environment (recommended)

python -m venv venv
venv\Scripts\activate # On Windows

### 3. Install dependencies

pip install flask openai-whisper

### 4. Install and configure ffmpeg

- Download static build from [ffmpeg.org](https://ffmpeg.org/download.html)
- Extract to a folder (e.g., `C:\ffmpeg`)
- Add the `ffmpeg\bin` directory to your system PATH  

**Verify installation:**

ffmpeg -version

---

## Usage

### 1. Place your audio file

Copy your audio file (`Recording.wav`) to the project directory or change the path in `app.py` as needed.

### 2. Run the Flask app

python app.py

Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your browser.

---

## File Structure

audio-text-flask-app/
│
├── app.py
├── Recording.wav
├── requirements.txt
├── index.html # Your template
├── .gitignore
└── README.md

---

## Example Code Snippet

import os
os.environ["PATH"] += os.pathsep + r"C:\ffmpeg\bin" # Update with your ffmpeg bin path

from flask import Flask, render_template, send_file
import whisper

app = Flask(name)

def transcribe_audio(file_path):
model = whisper.load_model("base")
result = model.transcribe(file_path, word_timestamps=True)
return result["segments"]

@app.route('/')
def index():
audio_file_path = r"C:\Users\abhin\Desktop\My_Projects\Audio-Text Conversion\Recording.wav"
transcript_segments = transcribe_audio(audio_file_path)
return render_template('index.html', segments=transcript_segments)

@app.route('/audio')
def get_audio():
audio_file_path = r"C:\Users\abhin\Desktop\My_Projects\Audio-Text Conversion\Recording.wav"
return send_file(audio_file_path, mimetype='audio/wav')

if name == "main":
app.run(debug=True)

---

## Troubleshooting

- **WinError 2 / FileNotFoundError:**  
    Double-check your ffmpeg installation and make sure the bin path is correctly set in both your system PATH and the script.
- **Audio file not found:**  
    Confirm the path and name of your audio file are correct.

---

## License

MIT

---

## Author

PSAbhinav
