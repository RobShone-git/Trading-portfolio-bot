import pandas as pd
import numpy as np

def run_AESI(data):
    df = pd.DataFrame(data)

    # Input parameters
    length = 8
    alpha = 0.5

    # Generate some sample data (replace this with your actual data)
    close_prices = df['close']

    # Calculate Exponential Moving Average (EMA)
    ema = close_prices.ewm(span=length, adjust=False).mean()

    # Calculate the total price-ema difference
    sad = np.sum(close_prices - ema[-length:])

    # Calculate the Smoothing Factor
    smoothing_factor = alpha * (sad / length)

    # Calculate AESI
    aesi = ema + smoothing_factor

    # Plotting AESI Cloud
    Buy = True if aesi.iloc[-1] > ema.iloc[-1] else False
    Sell = False if Buy == 'True' else True

    print("AESI:", aesi.iloc[-1])
    print(f"Buy: {Buy}")
    print(f"Sell: {Sell}")

    return "Advanced Exponential Smoothing Indicator (AESI) [AstrideUnicorn] (8)", aesi.iloc[-1], int(Buy)
