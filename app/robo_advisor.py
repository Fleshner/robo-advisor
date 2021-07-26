# this is the "app/robo_advisor.py" file
# this is the "app/robo_advisor.py" file
import re

import requests
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

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED'
final_url = f'{url}&symbol={stock_symbol}&apikey={api}'

r = requests.get(final_url)
data = r.json()

print(data)