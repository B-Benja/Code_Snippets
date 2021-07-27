import smtplib
import datetime as dt
from random import randint
import pandas as pd


MY_EMAIL = "YOR EMAIL"
PASSWORD = "YOUR PASSWORD"

# get current day and month
today_day = dt.datetime.now().day
today_month = dt.datetime.now().month

# Check if today matches a birthday in the birthdays.csv
birthday_data = pd.read_csv("birthdays.csv")
birth_dict = birthday_data.to_dict(orient="records")

birthday_wish = False

for entry in birth_dict:
    if entry["month"] == today_month and entry["day"] == today_day:
        today_birthday = entry
        to_email = today_birthday["email"]

        # pick a random letter from letter templates and replace the [NAME] & [YEAR] from birthdays.csv
        with open(f"letter_templates/letter_{randint(1, 3)}.txt") as letter:
            chosen_letter = letter.read()

        custom_letter = chosen_letter.replace("[NAME]", today_birthday["name"])
        custom_letter = custom_letter.replace("[YEAR]", str(dt.datetime.now().year - today_birthday["year"]))

        #  send the generated letter to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as email:
            email.starttls()
            email.login(user=MY_EMAIL, password=PASSWORD)
            email.sendmail(from_addr=MY_EMAIL, to_addrs=to_email, msg=f"Subject: Birthday Wishes\n\n{custom_letter}")



