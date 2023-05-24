
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser

# import smtplib(for emailing)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >0 and hour < 12:
        speak("Good Morning")
        print("GOOD MORNING")
    if hour > 12 and hour < 18:
        speak("Good Afternoon")
        print("GOOD AFTERNOON")
     
    else:
        speak("Good Evening")
        print("GOOD EVENING")
    speak("I am Alfred, How may I help you sir")
    print("I am Alfred, How may I help you sir?")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1.5
        r.energy_threshold = 500
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-US')
        print(f"User said:{query}\n")
    except LookupError:
        print("Sir can you say that again please...")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Cyril\\Music\\phone music'
            speak(f"Starting music now")
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")
