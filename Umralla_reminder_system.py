import tkinter as tk
from tkinter import messagebox
import requests
import schedule
import time
import threading
import smtplib
from email.message import EmailMessage

API_KEY = "c319e74062fe9792cbe5db8ef2cce667"
EMAIL_SENDER = "mohd74689@gmail.com"
EMAIL_PASSWORD = "lxkglchpyrqcaejv"  # 🔐 Replace with your app password
EMAIL_RECEIVER = "nadeemzack09@gmail.com"

# GUI weather function


def get_weather(city_name):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch weather data: {e}")
        return None


def show_weather():
    city_name = city_entry.get()
    if not city_name:
        messagebox.showerror("Error", "Please enter a city name.")
        return

    weather_data = get_weather(city_name)
    if weather_data and weather_data.get("cod") != "404":
        main = weather_data["main"]
        weather_desc = weather_data["weather"][0]["description"]
        temp = main["temp"]
        pressure = main["pressure"]
        humidity = main["humidity"]

        weather_info = f"City: {city_name}\nTemperature: {temp}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%\nDescription: {weather_desc}"
        messagebox.showinfo("Weather Information", weather_info)
    else:
        messagebox.showerror("Error", "City Not Found")

# Email reminder function


def umbrellaReminder():
    CITY = "Delhi"
    print("Checking weather for", CITY)
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print("Error from weather API:", data.get("message"))
            return

        weather = data['weather'][0]['main']
        temp = data['main']['temp']

        print(f"Weather: {weather}, Temp: {temp}°C")

        if weather in ["Rain", "Clouds", "Thunderstorm"]:
            subject = f"☔ Umbrella Reminder for {CITY}"
            body = f"Weather today is {weather} with temperature {temp}°C.\nDon't forget your umbrella!"

            msg = EmailMessage()
            msg.set_content(body)
            msg['Subject'] = subject
            msg['From'] = EMAIL_SENDER
            msg['To'] = EMAIL_RECEIVER

            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                smtp.starttls()
                smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
                smtp.send_message(msg)

            print("📩 Email sent.")
        else:
            print("✅ Weather is clear.")
    except Exception as e:
        print("❌ Error:", e)

# Scheduling


def run_schedule():
    schedule.every(1).minutes.do(umbrellaReminder)  # for testing
    while True:
        schedule.run_pending()
        time.sleep(1)


# GUI Setup
root = tk.Tk()
root.title("Live Weather App + Email Reminder")
root.geometry("400x200")

city_label = tk.Label(root, text="Enter City Name:")
city_label.pack(pady=5)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

notify_button = tk.Button(root, text="Get Weather", command=show_weather)
notify_button.pack(pady=10)

# Start schedule thread
threading.Thread(target=run_schedule, daemon=True).start()

root.mainloop()
