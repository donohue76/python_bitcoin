# import blockchain library
from blockchain import exchangerates

# get the Bitcoin rates in various currencies
ticker = exchangerates.get_ticker()

# print the Bitcoin price fot every currency
print("Bitcoin Prices")
for k in ticker:
	print(k, ticker[k].p15min)

# Getting Bitcoin value for a particular amount and currency
btc = exchangerates.to_btc('EUR', 100)
print("\n100 euros in Bitcoin: %s" % btc)