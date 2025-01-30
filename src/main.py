import pandas as pd
import numpy as np
from src.data.fetch_stock_data import fetch_stock_data
from src.data.fetch_options_data import fetch_options_data
from src.data.feature_engineering import feature_engineering
from src.data.sentiment_analysis import sentiment_analysis
from src.models.keras_model import create_and_train_model
from src.utils.calculate_option_greeks import calculate_option_greeks
from src.utils.visualization import visualize_results
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error

def main() -> None:
    """Main function to execute the trading system workflow."""
    ticker = 'AAPL'
    period = '10y'

    # Fetch and preprocess data
    stock_data = fetch_stock_data(ticker, period)
    options_data = fetch_options_data(ticker)

    # Calculate option greeks
    delta, gamma, theta, vega, rho = calculate_option_greeks()

    # Perform feature engineering
    features_df = feature_engineering(stock_data, options_data)
    
    # Perform sentiment analysis
    sentiment = sentiment_analysis(ticker)
    features_df['sentiment'] = sentiment

    # Target variable (placeholder)
    target_df = pd.DataFrame({'target': [features_df['option_price'][0]]})

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features_df, target_df, test_size=0.2, random_state=42)

    # Scale the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Create and train the model
    model = create_and_train_model(X_train_scaled, y_train)

    # Make predictions
    predictions = model.predict(X_test_scaled)

    # Evaluate the model
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    print(f"MAE: {mae:.4f}, MSE: {mse:.4f}")
    
    # Visualize the results
    visualize_results(y_test, predictions)

if __name__ == "__main__":
    main()
