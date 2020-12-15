import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("CompteR: ", audio)

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening..")
        r.pause_threshold = 1.0
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You: {query}\n")
        
    except Exception as e:
        print(e)
        speak("Sorry, Could not recognize")
        return "None"
    return query