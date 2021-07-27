# ask for exercise and time/ distance
# store in google sheet

import requests
from datetime import datetime as dt

# to access nutrition API & SHEETY
NUTRITION_ID = "YOUR ID"
NUTRITION_KEY = "YOUR KEY"
NUTRITION_API = "https://trackapi.nutritionix.com"
WORKOUT_ENDPOINT = "/v2/natural/exercise"

SHEETY_USER = "YOUR USER"
SHEETY_PROJECT = "YOUR PROJECT NAME"
SHEETY_SHEETNAME = "YOUR SHEET NAME"
SHEETY_API = "https://api.sheety.co/" + SHEETY_USER + "/" + SHEETY_PROJECT + "/" + SHEETY_SHEETNAME
BEARER_TOKEN = "YOUR TOKEN"


# info about the user
GENDER = "YOUR DATA"
WEIGHT_KG = "YOUR DATA"
HEIGHT_CM = "YOUR DATA"
AGE = "YOUR DATA"


HEADER = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_KEY,
    "x-remote-user-id": "0",
}

WORKOUT_PARAMETERS = {
    "query": input("What exercise did you do? "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

workout = requests.post(url=f"{NUTRITION_API}{WORKOUT_ENDPOINT}", json=WORKOUT_PARAMETERS, headers=HEADER).json()


# post the workout data in google sheets using sheety
SHEETY_HEADER = {
    "Authorization": BEARER_TOKEN,
}

now = dt.now()
today = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")

SHEETY_PARAMETERS = {"workout":
    {
    "date": today,
    "time": current_time,
    "exercise": workout["exercises"][0]["name"].title(),
    "duration": workout["exercises"][0]["duration_min"],
    "calories": workout["exercises"][0]["nf_calories"],
    }
}

update_sheet = requests.post(url=SHEETY_API, json=SHEETY_PARAMETERS, headers=SHEETY_HEADER)