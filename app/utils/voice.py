import json
import queue
import sounddevice as sd

from vosk import Model, KaldiRecognizer

MODEL_PATH = "models/vosk-model-small-en-us-0.15"

model = Model(MODEL_PATH)

recognizer = KaldiRecognizer(model, 16000)

audio_queue = queue.Queue()


def callback(indata, frames, time, status):

    if status:
        print(status)

    audio_queue.put(bytes(indata))


def listen():

    print("🎤 Listening...")

    with sd.RawInputStream(
        samplerate=16000,
        blocksize=8000,
        dtype="int16",
        channels=1,
        callback=callback,
    ):

        while True:

            data = audio_queue.get()

            if recognizer.AcceptWaveform(data):

                result = json.loads(recognizer.Result())

                text = result.get("text", "").strip()

                if text:

                    print(f"You said: {text}")

                    return text.lower()