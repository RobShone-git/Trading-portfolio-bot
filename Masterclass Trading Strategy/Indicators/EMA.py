import pandas as pd

def run_EMA(data):
    df = pd.DataFrame(data)

    # Input parameters
    ema_period = 23

    # Calculate 200 EMA
    ema = df['close'].ewm(span=ema_period, adjust=False).mean()

    # Determine Buy and Sell Conditions
    buy_condition = (df['close'].iloc[-1] > ema.iloc[-1])
    sell_condition = (df['close'].iloc[-1] <= ema.iloc[-1])

    # Print final values
    print(f"{ema_period} EMA: {ema.iloc[-1]}")
    print("Buy Signal:", buy_condition)
    print("Sell Signal:", sell_condition)

    return "Super Secret 200 EMA (23)", ema.iloc[-1], int(buy_condition)


