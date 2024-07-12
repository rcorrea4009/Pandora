import datetime
import pyttsx3
import speech_recognition as sr
import webbrowser as wb
import wikipedia

engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

voicespeed = 150
engine.setProperty('rate',voicespeed)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause = r.listen(source)
        aduio = r.listen(source)
    
    try:
        print('Recognising...')
        query = r.recognize_google(aduio, language = 'en-us')
    except Exception as e:
        print('---')
        speak('Could you please say that again.')
        return '---'
    return query

def time():
    time = datetime.datetime.now().strftime('%H:%M:%S')
    speak(time)
    #print(time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("The current date is:")
    speak(day)
    speak(month)
    speak(year)

def wishme():
    speak("welcom back Rachel")

    hour = datetime.datetime.now().hour
    if(hour >= 6 and hour <= 12):
        speak("Good Morning")
    elif hour >= 12 and hour <= 18:
        speak("Good afternoon")
    elif hour > 18 and hour <=24:
        speak("Good evening")
    else:
        speak("Good evening")
    
    speak("How can I help you today")

def openChrome():
    url="https://www.google.co.in/"
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    speak("Opening Chrome")
    wb.get(chrome_path).open(url)


if __name__ == '__main__':

    wishme()
    while True:
        query = takecommand().lower()
        print(query)

        if "good morning" in query:
            speak("Good morning Rachel")
        elif "time" in query:
            time()
        elif "date" in query:
            date()
        elif "open chrome" in query:
            openChrome()
        elif "wikipedia" in query:
            speak('Searching.....')
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            speak(result)
