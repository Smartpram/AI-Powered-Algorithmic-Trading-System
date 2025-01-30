from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout

def create_and_train_model(X_train: pd.DataFrame, y_train: pd.Series) -> Sequential:
    """Create and train a simple LSTM model.
    
    Args:
        X_train (pd.DataFrame): Training features.
        y_train (pd.Series): Training target.
    
    Returns:
        Sequential: Trained Keras LSTM model.
    """
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    model.fit(X_train, y_train, epochs=100, batch_size=32)
    return model
