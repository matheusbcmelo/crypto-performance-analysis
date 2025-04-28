#%% Import Libraries

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# The "ccxt" library facilitates connection to various exchanges, including Binance
import ccxt
#%% Creating DataFrame

crypto = pd.DataFrame({
    'symbols': ["BTC/USDT", "ETH/USDT", "BNB/USDT", "SOL/USDT", "XRP/USDT", "AVAX/USDT"],
})
#%% Extracting Data from Binance

# Binance API configuration
binance = ccxt.binance()

# List of crypto to fetch data for
symbols = crypto['symbols'].tolist()  # Add other pairs as necessary
timeframe = '1M'  # Timeframe (1 month)

'''
Available timeframes:
'1m' - 1 minute
'1h' - 1 hour
'1d' - 1 day
'1w' - 1 week
'1M' - 1 month
'''

limit = 120  # Number of candles

# Create a list to store the data
all_data = []

# Loop to fetch data for each asset
for symbol in symbols:
    try:
        # Fetch OHLCV data from Binance
        OHLCV = binance.fetch_ohlcv(symbol, timeframe, limit=limit)
        
        print(f"\nSymbol: {symbol}")
        print(f"Number of candles retrieved: {len(OHLCV)}")
        print(f"Date range: {pd.to_datetime(OHLCV[0][0], unit='ms')} to {pd.to_datetime(OHLCV[-1][0], unit='ms')}")
        
        # Process all candles
        for candle in OHLCV:
            data = {
                'symbols': symbol,
                'timestamp': pd.to_datetime(candle[0], unit='ms'),
                'open': candle[1],
                'high': candle[2],
                'low': candle[3],
                'close': candle[4],
                'volume': candle[5]
            }
            all_data.append(data)
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")

# Convert to a DataFrame
crypto_monthly_price = pd.DataFrame(all_data)

# Calculating Average Price
crypto_monthly_price['average_price'] = round((crypto_monthly_price['high'] + crypto_monthly_price['low']) / 2, 2)

# Group by month and calculate the average price
crypto_monthly_price['timestamp'] = pd.to_datetime(crypto_monthly_price['timestamp']).dt.to_period('M')

print(crypto_monthly_price.info())
# %%
