import speech_recognition as sr
from gtts import gTTS
import os
import subprocess
import time

def record_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please start speaking...")
        audio = r.listen(source)
    return audio

def speech_to_text(audio):
    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

def text_to_speech(text, output_file="C:\\Users\\GSori\\OneDrive\\Documents\\4thYear\\DSPA\\AI_outputasdfadsf.wav"):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save(output_file)
    return output_file

def play_audio(audio_file):
    subprocess.call(["ffplay", "-nodisp", "-autoexit", audio_file])

if __name__ == "__main__":
    audio = record_audio()
    text = speech_to_text(audio)

    if text == "stop":
        print("Stopping the program...")
    else:
        print("Recognized text:", text)
        output_file = text_to_speech(text)
        print("AI-generated audio saved as:", output_file)
        play_audio(output_file)

    time.sleep(2)  # Pause to allow the audio to finish playing (optional)
