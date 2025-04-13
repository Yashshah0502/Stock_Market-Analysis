import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st
import yfinance as yf
from sklearn.preprocessing import MinMaxScaler

st.sidebar.title("Model Settings")
user_input = st.sidebar.text_input('Enter stock ticker:', 'AAPL')
start_date = st.sidebar.date_input("Start date", pd.to_datetime('2010-01-01'))
end_date = st.sidebar.date_input("End date", pd.to_datetime('2019-12-31'))

ticker_obj = yf.Ticker(user_input)
df = ticker_obj.history(start= start_date, end = end_date)

st.subheader(f'Data from {start_date} to {end_date}')
st.write(df.describe())

st.subheader('Closing Price vs Time Chart')
fig = plt.figure(figsize=(12,6))
plt.plot(df.Close)
st.pyplot(fig)


st.subheader('Closing Price vs Time Chart for 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)


st.subheader('Closing Price vs Time Chart for 100MA & 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(12,6))
plt.plot(ma100)
plt.plot(ma200)
plt.plot(df.Close)
st.pyplot(fig)

data_training = pd.DataFrame(df['Close'][0:int(len(df)*0.7)])
data_testing = pd.DataFrame(df['Close'][int(len(df)*0.7):len(df)])

scaler = MinMaxScaler(feature_range= (0,1))

data_training_array = scaler.fit_transform(data_training)

model = load_model('keras_model.h5')

past_100_days = data_training.tail(100)

final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
input_data = scaler.fit_transform(final_df)

x_test = [] 
y_test = []

for i in range(100,input_data.shape[0]):
    x_test.append(input_data[i-100 : i])
    y_test.append(input_data[i,0])

x_test,y_test = np.array(x_test), np.array(y_test)

y_predicted = model.predict(x_test)

scaler = scaler.scale_
scale_factor = 1/scaler[0]
y_predicted = y_predicted * scale_factor
y_test = y_test * scale_factor


st.subheader('Prediction Vs Original')
fig2 = plt.figure(figsize=(12,6))
plt.plot(y_predicted, 'b', label='Predicted Price')
plt.plot(y_test, 'r', label='Actual Price')
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.title(f'{user_input} Price Prediction')
plt.legend()
st.pyplot(fig2)
