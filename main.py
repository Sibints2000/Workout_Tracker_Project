import requests
from

GENDER = "male"
WEIGHT_KG = 55
HEIGHT_CM = 168
AGE = 21

NUTRI_APP_ID = "076ea41b"
NUTRI_API_KEY = "c13eec2beeb2141474e9c037be8fa7da"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
print(result)
