# check if it will rain in your area in the next couple of hours

import requests

api = "YOUR API FROM https://openweathermap.org/"
my_latitude = "51.44083"
my_longitude = "5.47778"

parameters = {
    "lat": my_latitude,
    "lon": my_longitude,
    "appid": api,
    "exclude": "current,minutely,daily"
}


weather_data = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters).json()
print(weather_data)

will_rain = False

for x in range(0,13):
    if weather_data["hourly"][x]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")