
### `src/data/fetch_stock_data.py`

```python
import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker: str, period: str) -> pd.DataFrame:
    """Fetch historical stock data using yfinance.
    
    Args:
        ticker (str): The stock ticker symbol.
        period (str): The period for historical data (e.g., '10y').
    
    Returns:
        pd.DataFrame: Historical stock data.
    """
    try:
        stock_data = yf.download(ticker, period=period)
        return stock_data
    except Exception as e:
        print(f"Failed to fetch stock data: {e}")
        return None
