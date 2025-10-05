import requests
import json

bitcoin_url = "https://api.coingecko.com/api/v3/simple/price"

response = requests.get(bitcoin_url, params = {"ids": "bitcoin", "vs_currencies": "usd"}, timeout = 10)
response.raise_for_status()


data = response.json()

print("BTC (USD): ", data["bitcoin"]["usd"])
