import tkinter as tk
from tkinter import messagebox
import requests

# OpenWeather API Key (Replace with your own)
API_KEY = "fba2da291185f718d6629214db5f2279"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Function to fetch and display weather data
def get_weather():
    city = city_entry.get()
    
    if not city:
        messagebox.showerror("Error", "Please enter a city name!")
        return

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_text.set(f"City: {data['name']}, {data['sys']['country']}\n"
                         f"Temperature: {data['main']['temp']}°C\n"
                         f"Humidity: {data['main']['humidity']}%\n"
                         f"Weather: {data['weather'][0]['description'].title()}\n"
                         f"Wind Speed: {data['wind']['speed']} m/s")
    else:
        messagebox.showerror("Error", "Invalid city name or API key!")

# Create main Tkinter window
root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")

# UI Components
tk.Label(root, text="Enter City Name:", font=("Arial", 12)).pack(pady=5)
city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", font=("Arial", 12), command=get_weather).pack(pady=10)

weather_text = tk.StringVar()
weather_label = tk.Label(root, textvariable=weather_text, font=("Arial", 12), justify="left")
weather_label.pack(pady=10)

# Run Tkinter event loop
root.mainloop()
