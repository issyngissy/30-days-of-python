import requests

URL = https://au.finance.yahoo.com/quote/BTC-USD/
page = requests.get(URL)

print(page.text)