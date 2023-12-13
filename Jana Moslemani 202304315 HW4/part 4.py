import openai
import json
import time
import speech_recognition as sr
import pyttsx3
import pyaudio
# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key


def turnOnMicrowave(delay):
    signal = {
        "action": "turn_on the microwave ",
        "delay": delay,
    }
    print(f"Signal sent: {json.dumps(signal)}")
    time.sleep(delay)
    return "Microwave turned on after delay."


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak your command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Command recognized: {command}")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, could not understand the command.")
        return None


def whisper(text):
    engine = pyttsx3.init()
    engine.setProperty('volume', 0.5) 
    engine.setProperty('rate', 150)   
    engine.setProperty('voice', 'english-us')  
    engine.setProperty('voice', engine.getProperty('voices')[1].id)  
    engine.save_to_file(text, 'whisper_output.mp3')  
    engine.runAndWait()


command = recognize_speech()
if command == 'turn on microwave':
    
    delay = 10
    response_result = turnOnMicrowave(delay)
    print(response_result)
    whisper("Your food is ready.")  
