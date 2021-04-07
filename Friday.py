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


def takeCommand():
    # it takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    # User query is converted to lower case


# Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia....')

            #query = query.replace("wikipedia", "")

            # Use Index.summary() function to find the summary of the Index.
            results = wikipedia.summary(query, sentences=10)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\user\\Desktop\\music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'thank you' in query:
            speak('Happy to help sir')

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            newname = takeCommand()
            speak("Thanks for naming me")
