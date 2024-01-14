import pandas as pd
import numpy as np

def run_kama(data):
    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Define input parameters
    fast_period = 7
    slow_period = 19
    er_period = 8
    norm_period = 50
    norm = True

    # Calculate the efficiency ratio
    change = np.abs(df['close'] - df['close'].shift(er_period))
    volatility = df['close'].diff(er_period).abs().sum()
    er = change / volatility

    # Calculate the smoothing constant
    sc = er * (2 / (fast_period + 1) - 2 / (slow_period + 1)) + 2 / (slow_period + 1)

    # Calculate the KAMA
    df['ema_fast'] = df['close'].ewm(span=fast_period, adjust=False).mean()
    kama = df['ema_fast'] + sc * (df['close'] - df['ema_fast'])

    # Normalize the oscillator
    if norm:
        lowest = kama.rolling(window=norm_period, min_periods=1).min()
        highest = kama.rolling(window=norm_period, min_periods=1).max()
        normalized = (kama - lowest) / (highest - lowest) - 0.5
    else:
        normalized = kama

    buy = normalized > 0
    sell = normalized <= 0

    # Print final values
    print(f"KAMA: {normalized.iloc[-1]}")
    print("Buy Signal:", buy.iloc[-1])
    print("Sell Signal:", sell.iloc[-1])

    return "Normalize Kama Oscillator", normalized.iloc[-1], int(buy.iloc[-1])