import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import json
import requests
import pyjokes


print("Loading your AI personal assistant G-One")
def username():
    speak("What should i call you sir")
    user_name=takeCommand()
    speak("Hello")
    speak(user_name)
#0 => male voice,1 => female voice

engine=pyttsx3.init('sapi5')
voices=engine.getProperty("voices")
engine.setProperty("voice","voices[0}.id")

def speak(text):
    engine.say(text)
    engine.runAndWait()




def wishMe():
    hour=datetime.datetime.now().hour

    if hour>=5 and hour<12:
        speak("Hello,Good Morning")
        print("Hello,Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Hello,Good Afternoon")
        print("Hello,Good Afternoon")

    elif hour>=18 and hour<22:
        speak("Hello,Good Evening")
        print("Hello,Good Evening")

    else:
        speak("Hello,Good Night")
        print("Hello,Good Night")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n ")

        except Exception as e:
            speak("Pardon me,please say that again")
            return "None"
        return statement


    

        
speak("Loading your AI personal assistant G-One")
username()
wishMe()


if __name__=='__main__':
    
    while True:
        speak("Tell me how can I help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue
        if "goodbye" in statement or "okay bye" in statement or "stop" in statement:
            speak("your personal assistant G-one is shutting down,Good bye")
            print("your personal assistant G-one is shutting down,Good bye")
            break


        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement=statement.replace("wikipedia","")
            results=wikipedia.summary(f"{statement}")
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail open now")
            time.sleep(5)

        #predicting time
        elif 'time' in statement:
            currentTime=datetime.datetime.now().strftime("%H %M %S")
            speak(f"the time is{currentTime}")
                                                    
        elif 'news' in statement:
            news=webbrowser.open_new_tab("https://www.bbc.com/turkce")
            speak("Here are news from the BBC")

        elif 'camera' in statement or 'take a photo' in statement:
            ec.capture(0,"robo camera","img.jpg")

        
        elif 'joke' in statement:
            speak(pyjokes.get_joke())

        elif 'where is' in statement:
            statement=statement.replace("where is","")
            location=statement
            speak("You are asked to locate")
            speak(location)
            location=webbrowser.open("https://www.google.nl/maps" + location + "")


            








