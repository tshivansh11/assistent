# module
from time import strftime
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
 

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')#getting details of current voice
engine.setProperty('voice',voices[0].id)
print(voices)
# to speak and add sum audio
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# wish me function after the run code the wish you
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am potter sir. please tell me how may i help you")
def takeCommand():
    #it take microphone input form the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio=r.listen(source)
    try:
        #import pyaudio 
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"Use Said:{query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query                      

wishMe()
while True:
    query=takeCommand().lower()
    #logic for executing task based on query
    if ('wikipedia' in query):
        speak('Searching Wikipedia...')
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentences=2)
        speak("Accordig to Wikipedia")
        speak(results)
        print(results)
    if 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'play music' in query:
        music_dir= 'F:\\Mobile data\\Music\\punjabi songs'
        songs= os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[0]))
    elif 'the time' in query:
        strftime=datetime.datetime.now().strftime("%H:%M")
        speak(f"the time is{strftime}")