#import requests
#from bs4 import BeautifulSoup

#URL = "https://bitbo.io/"
##page = requests.get(URL)

#soup = BeautifulSoup(page.content, "html.parser")

#print(page.text)
#results = soup.find(id="top-stats")
#print(results.prettify())

#btc_amount = results.find_all("div", class_="amount")

#btc_amount = str(btc_amount)

#-----------------------------

#btc = btc_amount[32:38].strip().replace(",", "")

#btc = int(btc)
btc = int(74000)
ethereum = int(2777)
litecoin = int(70)

current_balance = int(100000)


btc_count = int(0)
ethereum_count = int(0)
litecoin_count = int(0)
while current_balance > btc:
    current_balance -= btc
    btc_count += 1
        
    

while current_balance > ethereum:
    current_balance -= ethereum
    print(current_balance)
    ethereum_count += 1
        

while current_balance > litecoin:
    current_balance -= litecoin
    litecoin_count += 1
        

total_crypto_spend = btc_count * btc + ethereum_count * ethereum + litecoin_count * litecoin


print("\n", "The amount of crypto you can buy is")
print("  bitcoin  ", btc_count, "\n", " ethereum ", ethereum_count, "\n", " litecoin ", litecoin_count)
print("\n", "The amount you will spent ", total_crypto_spend)
print(" Remaining balance ", current_balance, "\n")





