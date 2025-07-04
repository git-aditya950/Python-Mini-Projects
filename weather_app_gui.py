import tkinter as tk
import requests
from PIL import Image, ImageTk
from io import BytesIO

def get_weather():
    city = city_entry.get()
    api_key = "202de3ba1dc324adc420da39f914baca"  # Replace with your key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        icon_code = data['weather'][0]['icon']

        result_label.config(
            text=f"{city.title()}\n"
                 f"🌡 {temp}°C\n"
                 f"💧 {humidity}% Humidity\n"
                 f"💨 {wind} m/s\n"
                 f"☁ {weather.title()}",
            fg="#ffffff"
        )

        # Show weather icon
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
        icon_data = requests.get(icon_url).content
        icon_img = Image.open(BytesIO(icon_data))
        icon_photo = ImageTk.PhotoImage(icon_img)

        icon_label.config(image=icon_photo)
        icon_label.image = icon_photo

    else:
        result_label.config(text="⚠️ City not found or API error.", fg="red")
        icon_label.config(image="")

# -------------------- UI --------------------
root = tk.Tk()
root.title("🌦 Weather Forecast")
root.geometry("400x450")
root.configure(bg="#1e1e2e")

# Title
tk.Label(root, text="Weather App", font=("Segoe UI", 20, "bold"), fg="#ffffff", bg="#1e1e2e").pack(pady=15)

# Entry box
entry_frame = tk.Frame(root, bg="#1e1e2e")
entry_frame.pack()

city_entry = tk.Entry(entry_frame, font=("Segoe UI", 14), width=20, justify="center", bg="#2e2e3e", fg="#ffffff", borderwidth=0, relief="flat")
city_entry.pack(ipady=8, pady=5)
city_entry.insert(0, " ")

# Button
get_btn = tk.Button(root, text="Get Weather", command=get_weather, font=("Segoe UI", 12, "bold"), bg="#4f46e5", fg="white", relief="flat", padx=10, pady=6)
get_btn.pack(pady=15)

# Icon
icon_label = tk.Label(root, bg="#1e1e2e")
icon_label.pack()

# Result
result_label = tk.Label(root, text="", font=("Segoe UI", 14), bg="#1e1e2e", fg="white", justify="center")
result_label.pack(pady=10)

# Footer
tk.Label(root, text="Powered by OpenWeatherMap", font=("Segoe UI", 9), bg="#1e1e2e", fg="#aaaaaa").pack(side="bottom", pady=10)

root.mainloop()
