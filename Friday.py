import pyttsx3
# pyttsx3 is a text to speech conversion library in python


import speech_recognition as sr
import datetime
# to show currrent date and time

import time
import wikipedia
# wiki api used

import webbrowser
# inbuilt module

import os
import wolframalpha


engine = pyttsx3.init('sapi5')
# Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft


voices = engine.getProperty('voices')
# print(voices)
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
# voices[0] for male & voices[1] for female audio.


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!, Abhishek")
        # speak("Abhishek")
    elif hour >= 12 and hour <= 18:
        speak("Good Afternoon!, Abhishek")
        # speak("Abhishek")
    else:
        speak("Good Evening!, Abhishek")
        # speak("Abhishek")
    newname = ("Logitron online")
    speak(newname)
