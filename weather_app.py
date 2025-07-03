import requests

def get_weather(city):
    api_key = "202de3ba1dc324adc420da39f914baca"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    full_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    print(f"\n🔎 Requesting URL: {full_url}")  # Debug line
    response = requests.get(full_url)

    # Print raw response for debugging
    print("📦 Raw API Response:", response.text)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌤️ Weather in {city.title()}:")
        print(f"🌡️  Temperature: {temp}°C")
        print(f"💧  Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind_speed} m/s")
    else:
        print("\n❌ City not found or API error. Please check again.")

while True:
    print("\n🌐 Welcome to the Weather App!")
    city = input("Enter city name (or type 'exit' to quit): ")
    if city.lower() == 'exit':
        break
    get_weather(city)
