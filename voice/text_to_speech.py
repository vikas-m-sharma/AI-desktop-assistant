import asyncio
import edge_tts
from playsound import playsound
import os

def detect_language(text):
    # Detect Hindi characters
    for char in text:
        if "\u0900" <= char <= "\u097F":
            return "hi-IN-SwaraNeural"

    return "en-US-AriaNeural"

async def speak_async(text, voice):
    communicate = edge_tts.Communicate(text=text, voice=voice)
    await communicate.save("voice.mp3")

def speak(text):
    voice = detect_language(text)
    asyncio.run(speak_async(text, voice))
    playsound("voice.mp3")

    try:
        os.remove("voice.mp3")
    except:
        pass
