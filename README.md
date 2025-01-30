# AI-Powered Algorithmic Trading System (AATS)

## Description

This repository contains an AI-powered algorithmic trading system that employs machine learning and deep learning algorithms to generate trading signals for options on the stock ticker AAPL.

## Features

- Data Acquisition using `yfinance` and Alpha Vantage.
- Quantitative Analysis using engineered features and the Black-Scholes model.
- Model Development with Keras, including training, evaluation, and metrics (MAE and MSE).
- Sentiment Analysis using VADER on Yahoo Finance headlines.
- Visualization of Actual vs Predicted values.

## Requirements

To run this code, please ensure you have the following Python packages installed:

- `pandas`
- `numpy`
- `yfinance`
- `alpha_vantage`
- `scikit-learn`
- `keras`
- `matplotlib`
- `requests`
- `beautifulsoup4`
- `nltk`

Install the dependencies via pip:

```bash
pip install pandas numpy yfinance alpha_vantage scikit-learn keras matplotlib requests beautifulsoup4 nltk

Usage
To run the script, execute:
python src/main.py

