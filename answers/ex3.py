import requests
from bs4 import BeautifulSoup

URL = "https://bitbo.io/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#print(page.text)
results = soup.find(id="top-stats")
#print(results.prettify())

btc_amount = results.find_all("div", class_="amount")

btc_amount = str(btc_amount)
print(btc_amount[32:41].strip())