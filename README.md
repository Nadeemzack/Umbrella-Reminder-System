# Umbrella-Reminder-System
☔ Umbrella Reminder System
Umbrella Reminder System is a Python-based weather notification tool that fetches real-time weather data from the OpenWeatherMap API and alerts users via email or desktop GUI if the weather conditions indicate rain, clouds, or thunderstorms. It's designed to ensure you never leave home without an umbrella on a rainy day!
🔧 Features
✅ Fetches real-time weather data for any city

✅ Automatically sends email reminders if rain or bad weather is predicted

✅ Simple Tkinter-based GUI to check live weather conditions

✅ Uses schedule to automate daily checks

✅ Clean integration with Gmail using App Passwords

🛠️ Technologies Used
Python 3

Tkinter (GUI)

Requests (API calls)

Schedule (task scheduling)

smtplib / email (for sending email)

OpenWeatherMap API
⚙️ How It Works
User enters a city name in the GUI to fetch live weather data.

A background scheduler checks weather every day (or every few minutes for testing).

If rain/clouds/thunderstorm is detected, an automatic email is sent to the user.

Email authentication is securely done using Gmail App Passwords.

🔐 Setup Instructions
Get your OpenWeatherMap API key

Enable 2-Step Verification on your Gmail

Generate a Gmail App Password

Replace your email credentials and API key in the code

Install dependencies:
