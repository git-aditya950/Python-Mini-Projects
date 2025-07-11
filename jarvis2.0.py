import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3
import speech_recognition as sr
import openai
import threading
import webbrowser
import datetime
import os

openai.api_key = "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"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def wait_for_wake_word():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while True:
            try:
                print("🔎 Listening for wake word...")
                audio = recognizer.listen(source, timeout=5)
                trigger = recognizer.recognize_google(audio).lower()
                if "hey jarvis" in trigger:
                    speak("Yes, how can I help you?")
                    return
            except:
                continue

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("🎤 Listening for command...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=6)
            command = recognizer.recognize_google(audio)
            return command
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Network error."
        except sr.WaitTimeoutError:
            return "Listening timed out."

def handle_smart_command(command):
    command = command.lower()

    if "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google."

    elif "time" in command:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {now}."

    elif "play music" in command:
        music_folder = "C:\\Users\\adity\\Music"  
        if os.path.exists(music_folder):
            songs = os.listdir(music_folder)
            if songs:
                os.startfile(os.path.join(music_folder, songs[0]))
                return "Playing music."
            else:
                return "No music files found."
        else:
            return "Music folder not found."

    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp Web."

    elif "open srm" in command:
        webbrowser.open("https://www.srmist.edu.in")
        return "Opening SRM website."

    return None

def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response['choices'][0]['message']['content']
        return answer.strip()
    except Exception as e:
        return "Sorry, I can't process that."

# 🖼️ JARVIS GUI
class JarvisApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("JARVIS - Wake Word AI Assistant")
        self.geometry("800x500")
        self.resizable(False, False)

        self.bg_image = Image.open("320927.jpg").resize((800, 500))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.frame.pack(pady=20)

        self.output_text = ctk.CTkTextbox(master=self.frame, width=700, height=300, corner_radius=8, font=("Consolas", 14))
        self.output_text.pack()

        self.button = ctk.CTkButton(master=self, text="🎙 Start Listening", command=self.start_listening, font=("Consolas", 16))
        self.button.pack(pady=20)

    def start_listening(self):
        threading.Thread(target=self.listen_loop).start()

    def listen_loop(self):
        while True:
            wait_for_wake_word()
            self.process_command()

    def process_command(self):
        command = listen_command()
        self.output_text.insert(tk.END, f"\nYou: {command}\n")
        self.output_text.update_idletasks()

        local_response = handle_smart_command(command)
        if local_response:
            self.output_text.insert(tk.END, f"Jarvis: {local_response}\n")
            speak(local_response)
        else:
            response = ask_openai(command)
            self.output_text.insert(tk.END, f"Jarvis: {response}\n")
            speak(response)

if __name__ == "__main__":
    app = JarvisApp()
    app.mainloop()
