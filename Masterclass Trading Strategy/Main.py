import Price_Data
import Transfer
from Indicators import EMA
from Indicators import AESI
from Indicators import Linear_Trend
from Indicators import Kama

BTC_temp = Price_Data.get_data("https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_BTC_USD/latest?period_id=1DAY&limit=200")
BTC_Data = {
    'close': BTC_temp[2],
    'high': BTC_temp[0],
    'low': BTC_temp[1]
}

ETH_temp = Price_Data.get_data("https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_ETH_USD/latest?period_id=1DAY&limit=200")
ETH_Data = {
    'close': ETH_temp[2],
    'high': ETH_temp[0],
    'low': ETH_temp[1]
}

ETH_BTC_temp = Price_Data.get_data("https://rest.coinapi.io/v1/ohlcv/BITSTAMP_SPOT_ETH_BTC/latest?period_id=1DAY&limit=200")
ETH_BTC_Data = {
    'close': ETH_BTC_temp[2],
    'high': ETH_BTC_temp[0],
    'low': ETH_BTC_temp[1]
}

def run_indicators(data):
    results = []

    # Add indicators here ...................................
    ema_result = EMA.run_EMA(data)
    aesi_result = AESI.run_AESI(data)
    kama_result = Kama.run_kama(data)
    # .......................................................

    # Append the results to the 2D array ....................
    results.append(ema_result)
    results.append(aesi_result)
    results.append(kama_result)
    # .......................................................

    return results

Transfer.values(run_indicators(ETH_BTC_Data), run_indicators(BTC_Data), run_indicators(ETH_Data))