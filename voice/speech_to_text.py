import sounddevice as sd
from scipy.io.wavfile import write
import whisper
import tempfile
import os
import time

# Use base for better accuracy (you can keep tiny if speed preferred)
model = whisper.load_model("base")

def listen(samplerate=16000, duration=8):
    print("Listening... Speak now.")

    recording = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1
    )

    sd.wait()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        write(temp_file.name, samplerate, recording)
        temp_filename = temp_file.name

    result = model.transcribe(temp_filename)

    text = result["text"].strip()

    time.sleep(0.3)

    try:
        os.remove(temp_filename)
    except:
        pass

    # Smart fallback detection
    if not text or len(text) < 4:
        return ""

    print("You said:", text)
    return text
