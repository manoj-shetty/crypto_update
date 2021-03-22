import requests
import time
while True:
    rep = requests.get("https://api.binance.com/api/v3/ticker/24hr")
    max_change = 0.0
    print("Total number of coins:{}".format(len(rep.json())))
    max_change_crypto = ""
    for in_json in rep.json():
        try:
            price_change = round(float(in_json["priceChangePercent"]), 2)
            if price_change > max_change:
                max_change = price_change
                max_change_crypto = in_json["symbol"]
        except:
            continue
    print("Max Change Crypto:{}".format(max_change_crypto))
    print("Max Change :{}".format(max_change))
    time.sleep(3)

