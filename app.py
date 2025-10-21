import os

# Add the path to your ffmpeg 'bin' folder here. Update as needed.
os.environ["PATH"] += os.pathsep + r"C:\Users\abhin\Downloads\ffmpeg-2025-10-19\ffmpeg\bin"

# Verify ffmpeg is accessible
import subprocess
print("FFmpeg version check:")
ffmpeg_check = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
print(ffmpeg_check.stdout)
print(ffmpeg_check.stderr)

from flask import Flask, render_template, send_file
import whisper

app = Flask(__name__)

# Whisper transcription function with timestamps
def transcribe_audio(file_path):
    model = whisper.load_model("base")
    # Transcribing with timestamps
    result = model.transcribe(file_path, word_timestamps=True)
    return result["segments"]  # The segments will include timestamps

# Route to serve the webpage
@app.route('/')
def index():
    # Use the correct path for your audio file!
    audio_file_path = r"C:\Users\abhin\Desktop\My_Projects\Audio-Text Conversion\Recording.wav"
    if not os.path.exists(audio_file_path):
        return f"Audio file not found: {audio_file_path}", 404
    # Transcribe the audio
    transcript_segments = transcribe_audio(audio_file_path)
    return render_template('index.html', segments=transcript_segments)

# Route to serve the audio file
@app.route('/audio')
def get_audio():
    audio_file_path = r"C:\Users\abhin\Desktop\My_Projects\Audio-Text Conversion\Recording.wav"
    if not os.path.exists(audio_file_path):
        return f"Audio file not found: {audio_file_path}", 404
    return send_file(audio_file_path, mimetype='audio/wav')

if __name__ == "__main__":
    app.run(debug=True)
