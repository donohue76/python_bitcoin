# import blockchain library
from blockchain import statistics

# get the stats object
stats = statistics.get()
print("Bitcoin Trade Volume: %s" % stats.trade_volume_btc)

# get and print Bitcoin mined
print("Bitcoin mined: %s\n", stats.btc_mined)

# get and print Bitcoin market price in USD
print(stats.market_price_usd)