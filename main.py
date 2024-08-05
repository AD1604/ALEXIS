
import speech_recognition as sr
from time import ctime
import webbrowser
import time
import os
import random
from gtts import gTTS
import pygame

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak("SORRY !! didn't get that")
        except sr.RequestError:
            alexis_speak("APOLOGIES! my speech service is down")
        return voice_data

def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    random_str = random.randint(1, 1000000000)
    audio_file = 'audio' + str(random_str) + '.mp3'
    tts.save(audio_file)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    pygame.mixer.music.unload()
    pygame.quit()

    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if "what is your name" in voice_data:
        alexis_speak("My name is ALEXIS!")
    if "how are you " in voice_data:
        alexis_speak("i am well and good , how are you?")
    if "what time is it" in voice_data:
        alexis_speak(ctime())
    if "search" in voice_data:
        search = record_audio("WHAT DO YOU WANT TO SEARCH FOR?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak(f"Here is what I found for {search}")
    if "find location" in voice_data:
        location = record_audio("WHAT IS THE LOCATION?")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak(f"Here is the location of {location}")
    if "exit" in voice_data:
        alexis_speak("Goodbye!")
        exit()

time.sleep(1)
alexis_speak("HII IT'S ALEXIS \n HOW MAY I HELP YOU")
while True:
    voice_data = record_audio()
    respond(voice_data)
