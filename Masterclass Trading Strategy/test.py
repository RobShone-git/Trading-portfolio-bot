import pandas as pd
import requests
import json
import numpy as np

url = "https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_ETH_BTC/latest?period_id=1DAY&limit=200"

payload={}
headers = {
  'Accept': 'text/plain',
  'X-CoinAPI-Key': 'XXXXXXX'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)

print(data)
