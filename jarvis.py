import pyttsx3 as pt
import datetime as dt
import speech_recognition as sr
import wikipedia
import webbrowser
import os


engine = pt.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(dt.datetime.now().hour)
    if hour>=0 and hour>12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak('Good afternoon')
    else:
        speak('Good evening')  

    speak('I am Jarvis Sir. Please tell me how may I help you.') 

def takeCommand():
    # It takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')   
        r.pause_threshold = 1  
        audio=r.listen(source)

    try:
        print('Recognizing...') 
        query=r.recognize_google(audio)
        print(f"User said: {query}\n")
    except Exception as e:
        print("I could not get it. Say that again please...or contact my boss Sudhanshu Sir")   
        return "None" 
    return query   

           

if __name__ =="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
    # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackeverflow' in query:
            webbrowser.open('stackoverflow.com')   
            
        elif 'play music' in query:
            music_dir ='C:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=dt.datetime.now().strftime("%H:%M:%S") 
            speak(f"Sir, the time is {strTime}")   

        elif 'open code' in query:
            Path = "C:\\Users\\sudha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
            os.startfile(Path)

        elif 'open telegram' in query:
            Path = "C:\\Users\\sudha\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(Path)

        elif 'quit' in query:
            exit()    

