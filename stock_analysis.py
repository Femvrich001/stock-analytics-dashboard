import requests
import pandas as pd

# Replace with your own API key
api_key = 'XDN11D17JY83PDYG'

def fetch_stock_data(symbol):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    # Check if the data is available
    if 'Time Series (Daily)' in data:
        df = pd.DataFrame(data['Time Series (Daily)']).T
        df = df.astype(float)
        df.index = pd.to_datetime(df.index)
        return df
    else:
        return None

# Test the function
symbol = 'AAPL'
data = fetch_stock_data(symbol)
print(data.head())


def calculate_moving_averages(df):
    df['50_MA'] = df['4. close'].rolling(window=50).mean()
    df['200_MA'] = df['4. close'].rolling(window=200).mean()
    return df
