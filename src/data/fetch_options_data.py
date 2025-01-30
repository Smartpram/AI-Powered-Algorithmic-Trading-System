import yfinance as yf
import pandas as pd

def fetch_options_data(ticker: str) -> list:
    """Fetch options data for a specific ticker.
    
    Args:
        ticker (str): The stock ticker symbol.
    
    Returns:
        list: Options data information.
    """
    try:
        options_data = yf.Ticker(ticker).options
        return options_data
    except Exception as e:
        print(f"Failed to fetch options data: {e}")
        return None
