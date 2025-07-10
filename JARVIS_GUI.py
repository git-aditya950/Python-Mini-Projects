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

# 🔑 Replace with your actual OpenAI API Key
openai.api_key = "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"

# 🎤 Text-to-Speech Setup
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use female voice

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

# 🎙️ Speech Recognition
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)
            command = recognizer.recognize_google(audio)
            return command
        except sr.UnknownValueError:
            return "Sorry, I did not understand that."
        except sr.RequestError:
            return "Network error."
        except sr.WaitTimeoutError:
            return "Listening timed out."

# 🧠 Smart Offline Commands
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
        music_folder = "C:\\Users\\adity\\Music"  # 🔁 Change to your path
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
        webbrowser.open("https://srmist.edu.in")
        return "Opening SRM official website."

    return None  # Unknown command → forward to ChatGPT

# 🌐 OpenAI GPT Response
def ask_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response['choices'][0]['message']['content']
        return answer.strip()
    except Exception as e:
        print("❌ OpenAI error:", e)
        return "Sorry, I can't process that."

# 🖼️ JARVIS GUI
class JarvisApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("JARVIS - AI Assistant")
        self.geometry("800x500")
        self.resizable(False, False)

        # Background
        self.bg_image = Image.open("320927.jpg").resize((800, 500))
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        self.bg_label = tk.Label(self, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame
        self.frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.frame.pack(pady=20)

        # Text Output Box
        self.output_text = ctk.CTkTextbox(master=self.frame, width=700, height=300, corner_radius=8, font=("Consolas", 14))
        self.output_text.pack()

        # Button
        self.button = ctk.CTkButton(master=self, text="🎙 Activate Jarvis", command=self.activate_jarvis, font=("Consolas", 16))
        self.button.pack(pady=20)

    def activate_jarvis(self):
        threading.Thread(target=self.process_command).start()

    def process_command(self):
        command = listen_command()
        self.output_text.insert(tk.END, f"\nYou: {command}\n")
        self.output_text.update_idletasks()

        response = handle_smart_command(command)
        if response:
            self.output_text.insert(tk.END, f"Jarvis: {response}\n")
            speak(response)
        else:
            answer = ask_openai(command)
            self.output_text.insert(tk.END, f"Jarvis: {answer}\n")
            speak(answer)

# 🏁 Run App
if __name__ == "__main__":
    app = JarvisApp()
    app.mainloop()
