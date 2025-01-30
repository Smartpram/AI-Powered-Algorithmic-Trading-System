import matplotlib.pyplot as plt

def visualize_results(y_test: pd.Series, predictions: np.ndarray) -> None:
    """Plot the actual vs predicted values.
    
    Args:
        y_test (pd.Series): Actual values.
        predictions (np.ndarray): Predicted values.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(y_test.values, label='Actual')
    plt.plot(predictions, label='Predicted', alpha=0.7)
    plt.title('Actual vs Predicted Values')
    plt.xlabel('Samples')
    plt.ylabel('Values')
    plt.legend()
    plt.show()
