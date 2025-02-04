import requests
import json
import numpy as np

def get_data(link):

  url = link

  payload={}
  headers = {
    'Accept': 'text/plain',
    'X-CoinAPI-Key': 'XXXXXXXX'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  data = json.loads(response.text)

  price_high_values = [entry["price_high"] for entry in data]
  price_low_values = [entry["price_low"] for entry in data]
  price_close_values = np.flip([entry["price_close"] for entry in data])

  return price_high_values, price_low_values, price_close_values
