import requests
from bs4 import BeautifulSoup


URL = "https://bitbo.io/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="top-stats")
btc_amount = results.find_all("div", class_="amount")
btc_amount = str(btc_amount)

#-----------------------------

btc = btc_amount[32:38].strip().replace(",", "")
btc = int(btc) 
btc = 75000
ethereum = int(2777)
litecoin = int(70)

current_balance = int(7548938)

btc_count = int(0)
ethereum_count = int(0)
litecoin_count = float(0)



while current_balance > btc:
    current_balance -= btc
    btc_count += 1

while current_balance > ethereum:
    current_balance -= ethereum
    ethereum_count += 1    

while current_balance > litecoin:
    current_balance -= litecoin
    litecoin_count += 1

litecoin_count += current_balance / litecoin 
current_balance -= current_balance 

total_crypto_spend = btc_count * btc + ethereum_count * ethereum + litecoin_count * litecoin

print("\n", "The amount of crypto you can buy is")
print(" bitcoin  ", btc_count, "      @ price $", btc)
print(" ethereum ", ethereum_count, "      @ price $", ethereum)
print(" litecoin ", litecoin_count, "    @ price $", litecoin)
print("\n", "The amount you will spend ", total_crypto_spend)
print(" Remaining balance ", current_balance, "\n")





