import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
#pip install pocketsphinx

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "c3cc1b29-c0ad-48d3-b5ed-79cf64a520a2"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif(c.lower().startswith("play")):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
if __name__ == "__main__":
    speak("Initializing Sanika.....")
    #Listen for wake word "Novasanik"
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
       
        print("recognizing..")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)

            if(word.lower()=="sanika"):
                speak("Ya")
                #listen for command
                with sr.Microphone() as source:
                    print("Sanika Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))