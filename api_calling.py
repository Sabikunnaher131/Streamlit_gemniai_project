import google.generativeai as genai
from dotenv import load_dotenv
import os, io
from gtts import gTTS

load_dotenv()

genai.configure(api_key=os.getenv("GEMENI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def note_generator(images):
    prompt = """Summarize the picture in Bangla (max 100 words) with markdown formatting"""
    response = model.generate_content([images, prompt])
    return response.text


def audio_transcription(text):
    speech = gTTS(text, lang='bn', slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer


def quiz_generator(image, difficulty):
    prompt = f"Generate 3 quizzes based on {difficulty}, include answers and markdown formatting"
    response = model.generate_content([image, prompt])
    return response.text