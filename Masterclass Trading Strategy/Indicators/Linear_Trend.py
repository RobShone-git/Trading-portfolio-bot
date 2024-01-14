import pandas as pd
import numpy as np

# Function to calculate linear regression
def linreg(X, Y):
    a, b = np.polyfit(X, Y, 1)
    return a + b * X


def run_Linear_Trend(data):
    # Convert data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Linear regression parameters
    length = 70
    offset = 0
    deviation = 2

    # Calculate linear regression
    lreg = linreg(df['close'], np.arange(len(df)) + offset)
    lreg_x = linreg(df['close'], np.arange(len(df)) + offset + 1)

    # Calculate trend lines
    b = np.arange(len(df))
    s = lreg - lreg_x
    intr = lreg - b * s

    # Calculate standard deviation
    dS = np.sum((df['close'] - (s * (b - offset) + intr))**2)
    de = np.sqrt(dS / len(df))

    # Calculate upper and lower bounds
    up = (-de * deviation) + lreg
    down = (de * deviation) + lreg

    # Calculate trend direction
    up_t = np.zeros_like(df['close'])
    down_t = np.zeros_like(df['close'])

    for i in range(1, len(df)):
        up_t[i] = max(up[i], up_t[i-1]) if df['close'][i-1] > up_t[i-1] else up_t[i-1]
        down_t[i] = min(down[i], down_t[i-1]) if df['close'][i-1] < down_t[i-1] else down_t[i-1]

    trend = np.zeros_like(df['close'])

    for i in range(1, len(df)):
        trend[i] = 1 if df['close'][i] > down_t[i-1] else -1 if df['close'][i] < up_t[i-1] else trend[i-1]

    r_line = np.where(trend == 1, up_t, down_t)

    buy = df['close'] > r_line
    sell = df['close'] < r_line

    print("Linear Trend:", r_line)
    print(f"Buy: {buy.iloc[-1]}")
    print(f"Sell: {sell.iloc[-1]}")

    return "idk", r_line, int(buy)
