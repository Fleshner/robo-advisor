# this is the "app/robo_advisor.py" file
# this is the "app/robo_advisor.py" file
import json
import re
import requests
import statistics
print("-------------------------")
x = input("Select your symbol:")
print("Stock symbol selected:", x)
print("Let me look that up for you...")

#Stackoverflow.com with the assist
#(https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths)
if not re.match("^[A-Z]*$", x):
    print("Error! Only letters A-Z allowed!.. Start Over")
    exit()
elif(len(x) > 5):
    print("Error! Stock symbols are 5 characters or less... Start over")
    exit()

import requests
import os
from dotenv import dotenv_values
from dotenv.main import load_dotenv
load_dotenv()

api = os.getenv("api_key")
stock_symbol = x

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED'
final_url = f'{url}&symbol={stock_symbol}&apikey={api}'

import pandas as pd
import csv

r = requests.get(final_url)
parsed_response = json.loads(r.text)

#Got to this point before I needed to consult with the screencast for some added guidance. Thank you!


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd)


last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
dates = list(tsd.keys()) 

latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"] 

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price)) #converted string
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices)

#
# INFO OUTPUTS
#
csv_file_path = "data/prices.csv"
csv_headers = ["timestamp", "open", "high", "low", "close"]

with open(csv_file_path, "w") as csv_file: 
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
        })

if float(latest_close) < statistics.mean(high_prices):
    recommendation = "Buy"
elif float(latest_close) > statistics.mean(high_prices):
    recommendation = "Sell"

if recommendation == "Buy":
    reason = "The close is lower than the average high in the dataset."

if recommendation == "Sell":
    reason = "The close is higher than the average high in the dataset."

print("-------------------------")
print("SELECTED SYMBOL:", x)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY:", latest_day)
print("LATEST CLOSE:", latest_close)
print("RECENT HIGH:", recent_high)
print("RECENT LOW:", recent_low)
print("-------------------------")
print("RECOMMENDATION:", recommendation)
print("RECOMMENDATION REASON:", reason)
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")