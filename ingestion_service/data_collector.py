import requests
import json

API_URL = "https://www.alphavantage.co/query"
API_KEY = "your_api_key"  # Необходимо зарегистрироваться на Alpha Vantage

def fetch_stock_data(symbol):
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {symbol}")
        return None

if __name__ == "__main__":
    symbol = "AAPL"
    data = fetch_stock_data(symbol)
    if data:
        with open(f"{symbol}_data.json", "w") as f:
            json.dump(data, f)
        print(f"Data for {symbol} saved.")
