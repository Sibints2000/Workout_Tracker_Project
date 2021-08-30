import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 55
HEIGHT_CM = 168
AGE = 21

NUTRI_APP_ID = "076ea41b"
NUTRI_API_KEY = "c13eec2beeb2141474e9c037be8fa7da"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": NUTRI_APP_ID,
    "x-app-key": NUTRI_API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
