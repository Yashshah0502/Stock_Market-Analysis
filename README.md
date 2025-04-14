# Stock Price Prediction App

A web application built with Streamlit that predicts stock prices using LSTM (Long Short-Term Memory) neural networks.

## Overview

This application allows users to visualize historical stock data and make price predictions using a pre-trained LSTM model. The app fetches stock data using Yahoo Finance API and displays various visualizations including moving averages and price predictions compared to actual values.

## Features

- Interactive stock ticker selection
- Customizable date range selection
- Data visualization with various moving averages (100-day and 200-day)
- Stock price prediction using a pre-trained LSTM neural network model
- Comparison of predicted vs actual prices

## Project Structure

```
├── app.py                  # Streamlit application code
├── keras_model.h5          # Trained LSTM model
├── LSTM.ipynb    # Jupyter notebook for model creation and training
└── README.md               # Project documentation
```

## Prerequisites

- Python 3.7+
- Required Python packages (see Installation section)

## Installation

1. Clone this repository
```bash
git clone https://github.com/Yashshah0502/stock-prediction-app.git
cd stock-prediction-app
```

2. Install the required packages
```bash
pip install -r requirements.txt
```

## Dependencies

The following Python packages are required:
- pandas
- numpy
- matplotlib
- pandas-datareader
- keras
- tensorflow
- streamlit
- yfinance
- scikit-learn

You can install all dependencies using:
```bash
pip install pandas numpy matplotlib pandas-datareader keras tensorflow streamlit yfinance scikit-learn
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and go to `http://localhost:8501`

3. Enter a stock ticker symbol in the sidebar (default is 'AAPL')

4. Select start and end dates for the data range

5. The app will display stock information and predictions automatically

## Model Information

The stock price prediction model is built using LSTM (Long Short-Term Memory) neural networks, which are particularly effective for time-series forecasting. The model was trained on historical stock data with the following characteristics:

- Built with Keras/TensorFlow
- Uses 100 days of historical closing prices to predict the next day's price
- Data is normalized using Min-Max scaling before training
- The model is trained on 70% of the available data
- Predictions are evaluated against the remaining 30% of data

The LSTM model is created and trained in the `LSTM.ipynb` Jupyter notebook and saved as `keras_model.h5`.

## How It Works

1. The app fetches historical stock data for the specified ticker and date range
2. It displays statistical information about the stock data
3. Various charts visualize the closing price and moving averages
4. The app loads the pre-trained LSTM model
5. Using the last 100 days of the training data, the model makes predictions for the test period
6. The predictions are plotted against the actual prices for visual comparison

## Limitations

- The model is trained on historical data and may not account for sudden market changes or unexpected events
- Prediction accuracy can vary significantly between different stocks and market conditions
- The app uses a pre-trained model and does not retrain on new data automatically

## Future Improvements

- Add real-time data updates
- Implement model retraining on new data
- Include more technical indicators for visualization
- Add performance metrics for model evaluation
- Support for cryptocurrency and other financial instruments

## Acknowledgments

- Yahoo Finance API for providing stock data
- Keras and TensorFlow for the deep learning framework
- Streamlit for the web application framework
