import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import sys
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 1].id)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")


wishMe()
speak('Phoebe is here. How may I help you?')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        return query.lower()
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        return str(input('Command: '))


if __name__ == '__main__':
    while True:
        query = takeCommand()

        if 'open my page' in query:
            speak('Okay')
            webbrowser.open('http://www.parasarpaudel.com.np')

        elif 'open google' in query:
            speak('Okay')
            webbrowser.open('http://www.google.co.in')

        elif "weather update" in query or "what is the weather today" in query or "weather forecast" in query:
            speak("Okay")
            webbrowser.open("https://www.accuweather.com/en/np/nepal-weather")

        elif 'open youtube' in query:
            speak('Okay')
            webbrowser.open('http://www.youtube.com')

        elif 'open gmail' in query:
            speak('Okay')
            webbrowser.open('http://www.gmail.com')

        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!']
            speak(random.choice(stMsgs))

        elif 'who created you' in query:
            speak('Parashar created me')

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("The time is %I:%M %p")
            speak(strTime)

        elif "best place to visit near Kathmandu" in query:
            speak("Shivapuri, Taudaha, Swayambhunath, White Gumba, Lakuri Bhanjyang, Namobuddha, Durbar Squares, "
                  "Kakani, Sundarijal, Godawari, and so on")

        elif 'what is your future plan' in query:
            speak("I don't even have a plan")

        elif "open visual studio code" in query:
            codePath = r"C:\Users\Mr. Pariskrit paudel\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            speak('Who is the recipient?')
            recipient = takeCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say?')
                    content = takeCommand()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except Exception as e:
                    speak('Sorry Sir! I am unable to send your message at this moment.')

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('Okay, have a great day, sir.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'sing me a song' in query:
            speak("Don't you have your own playlist?")

        elif 'bye' in query:
            speak('Bye Sir, see you soon.')
            sys.exit()

        elif "location" in query or "place near me" in query:
            speak('Okay')
            webbrowser.open('https://www.google.com/maps/place/Nepal')

        elif 'play music' in query:
            music_dir = r"D:\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[2]))
            speak('Enjoy your music')

        else:
            speak('Searching...')
            try:
                results = wikipedia.summary(query, sentences=2)
                speak('Got it.')
                speak('According to Wikipedia - ')
                speak(results)
            except Exception as e:
                webbrowser.open('http://www.google.com')
