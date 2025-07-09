import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

engine = pyttsx3.init()

voices = engine.getProperty('voices')
for voice in voices:
    if "english" in voice.name.lower() and "uk" in voice.name.lower():
        engine.setProperty('voice', voice.id)
        break
engine.setProperty('rate', 150) 

def speak(text):
    print(f"🧠 Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("I didn’t catch that. Could you please repeat?")
        return ""
    except sr.RequestError:
        speak("Speech service is unavailable at the moment.")
        return ""


def run_jarvis():
    speak("Hello, I am Jarvis. How may I assist you today?")

    while True:
        command = listen()

        if command == "":
            continue

        elif "play" in command:
            song = command.replace("play", "").strip()
            if song:
                speak(f"Playing {song} on YouTube.")
                pywhatkit.playonyt(song)
            else:
                speak("Please tell me the song name.")

        elif "time" in command or "what time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif "exit" in command or "stop" in command or "thank you" in command:
            speak("Goodbye, Sir. Shutting down.")
            break
        else:
            speak("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    run_jarvis()
