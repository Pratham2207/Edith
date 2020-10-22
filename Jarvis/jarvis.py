import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import random
import datetime
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning sir, Edith online")
        elif hour >= 12 and hour < 18:
                speak("Good Afternoon sir, Edith here")
        else:
                    speak("Good Night sir, Edith out")


def takecom():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        audio = r.listen(source)
        try:
            print("Recognizing")
            text = r.recognize_google(audio,language='en-in')
            print(text)
        except Exception:
             speak("error....")
             print("Network error")
             return "none"
        return text
                
    

if __name__ == "__main__":
            wish()
            while True:
                query  = takecom().lower()
                
                if "wikipedia" in query:
                    speak("Searching details.....Please Wait")
                    query.replace("wikipedia","")
                    results = wikipedia.summary(query,sentences=2)
                    print(results)
                    speak(results)
                elif 'open youtube' in query or "open video online" in query:
                        webbrowser.open("www.youtube.com")
                        speak("open youtube")
                elif 'open google' in query or "search google" in query:
                        webbrowser.open("www.google.co.in")
                        speak("opening google")
                elif 'bye' in query:
                        speak("Bye sir, Edith out")
                        exit()
                elif "shutdown" in query:
                        speak("Ok sir. Shutting down the system")
                        os.system('shutdown -s')
                elif 'open github' in query:
                    webbrowser.open("google.com.github.com")
                    speak("Yes sir, opening your github")
                elif 'open facebook' in query:
                    speak("Ok sir, opening facebook")
                    webbrowser.open("http://www.facebook.com/")
                elif 'open white hat' in query:
                    speak("opening whitehat")
                    webbrowser.open("https://www.whitehatjr.com/")
                elif'who are you' in query:
                    speak("I am edith, a programme created by my owner Pratham")
                elif 'what can you do'in query:
                    speak("I can open many websites and open applications like vs code and can search anything for you in wikipedia")
                elif 'open vs code' in query:
                    speak("opening vs code")
                    codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                    os.startfile(codePath)
                elif  'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir,the time is {strTime}")
               
