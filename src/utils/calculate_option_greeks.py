import numpy as np

def calculate_option_greeks() -> tuple:
    """Simulate calculation of option greeks.
    
    Returns:
        tuple: Simulated values for delta, gamma, theta, vega, and rho.
    """
    delta = np.random.uniform(0.1, 0.9)
    gamma = np.random.uniform(0.01, 0.1)
    theta = np.random.uniform(-0.1, -0.01)
    vega = np.random.uniform(0.01, 0.1)
    rho = np.random.uniform(0.01, 0.1)
    return delta, gamma, theta, vega, rho
