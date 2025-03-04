import speech_recognition as sr
import webbrowser
import pyttsx3
#pip install pocketsphinx

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Saanika.....")
    #Listen for wake word "Novasanik"
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
       
        print("recognizing..")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)

            command = r.recognize_google(audio)
            if(command.lower()=="Saanika"):
                speak("Ya")
                #listen for command
            print(command)
        except Exception as e:
            print("Error; {0}".format(e))