import requests

API_KEY = "55ce6bbf53a17f1dad8960e1b4807484"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

data = response.json()

if response.status_code == 200:

    print("\nWeather Information")
    print("---------------------")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Wind Speed:", data["wind"]["speed"], "m/s")
    print("Condition:", data["weather"][0]["description"])

else:
    print("City not found or API key invalid!")