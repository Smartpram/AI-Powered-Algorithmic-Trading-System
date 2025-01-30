import requests
from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment_analysis(ticker: str) -> float:
    """Fetch and analyze sentiment from Yahoo Finance news for the given ticker.
    
    Args:
        ticker (str): The stock ticker symbol.
    
    Returns:
        float: Average sentiment score.
    """
    try:
        url = f"https://finance.yahoo.com/quote/{ticker}/news/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find_all('h3')
        sia = SentimentIntensityAnalyzer()
        
        sentiments = []
        for headline in headlines:
            sentiment = sia.polarity_scores(headline.text)
            sentiments.append(sentiment['compound'])
        
        return np.mean(sentiments) if sentiments else 0.0
    except Exception as e:
        print(f"Failed to perform sentiment analysis: {e}")
        return 0.0
