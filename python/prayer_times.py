import requests
from datetime import datetime

adhan_url = "https://api.aladhan.com/v1/timingsByCity"

city =  input("Which city do you live in: ")
state =  input("Which state do you live in: ")
country = "United States"

params = {
        "city": city,
        "state": state,
        "country": country,
        "method": 2
}

response = requests.get(adhan_url, params = params, timeout = 10)
response.raise_for_status()
data = response.json()

print()

prayers = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]
print(f"Prayer times for {city}, {state} - {country}:")

for prayer in prayers:
    prayer_time = data["data"]["timings"][prayer]
    prayert_12 = datetime.strptime(prayer_time, "%H:%M").strftime("%I:%M %p")
    print(f"{prayer}: {prayert_12}")
#for prayer, time in data["data"]["timings"].items():
#    print(f"{prayer}: {time}")
