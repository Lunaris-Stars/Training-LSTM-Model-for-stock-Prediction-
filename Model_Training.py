import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM
from tensorflow.keras.callbacks import EarlyStopping

def analyze(data_1, ticker, time_step, epochs, learning_rate):
    if len(data_1) < 120:  # Assuming we need at least 120 data points for meaningful analysis
        st.warning(f"Insufficient data for {ticker}. Need at least 120 data points, but got {len(data_1)}.")
        return

    prices = data_1['Close'].values.reshape(-1, 1)
    scaler = MinMaxScaler(feature_range=(0, 1))
    prices_scaled = scaler.fit_transform(prices)

    train_size = int(len(prices_scaled) * 0.7)
    train_data, test_data = prices_scaled[:train_size], prices_scaled[train_size:]

    def data_to_input_and_output(data, time_step=1):
        input_data, output_data = [], []
        for i in range(len(data) - time_step - 1):
            input_data.append(data[i: (i + time_step), 0])
            output_data.append(data[i + time_step, 0])
        return np.array(input_data), np.array(output_data)

    X_train, Y_train = data_to_input_and_output(train_data, time_step=time_step)
    X_test, Y_test = data_to_input_and_output(test_data, time_step=time_step)

    if len(X_train) == 0 or len(X_test) == 0:
        st.warning(f"Insufficient data for {ticker} after preprocessing. Unable to train/test the model.")
        return

    X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

    model = Sequential([
        LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)),
        LSTM(units=50),
        Dense(units=1)
    ])

    model.compile(optimizer='adam', loss='mean_squared_error')

    model.fit(
        X_train, Y_train,
        epochs=epochs,  # Use the epochs parameter
        batch_size=32,
        callbacks=[EarlyStopping(monitor='val_loss', patience=20)]
    )

    # Evaluate the model
    train_loss = model.evaluate(X_train, Y_train, verbose=0)
    test_loss = model.evaluate(X_test, Y_test, verbose=0)
    st.write(f'Train Loss: {train_loss:.6f}')
    st.write(f'Test Loss: {test_loss:.6f}')

    train_predictions = model.predict(X_train)
    test_predictions = model.predict(X_test)

    train_predictions = scaler.inverse_transform(train_predictions)
    y_train_unscaled = scaler.inverse_transform(Y_train.reshape(-1, 1))
    test_predictions = scaler.inverse_transform(test_predictions)
    y_test_unscaled = scaler.inverse_transform(Y_test.reshape(-1, 1))

    test_start_index = len(train_predictions) + (time_step * 2)
    
    show_graph(data_1, train_predictions, test_predictions, y_train_unscaled, y_test_unscaled, time_step, test_start_index, ticker)

def show_graph(data, train_predictions, test_predictions, y_train_unscaled, y_test_unscaled, time_step, test_start_index, ticker):
    plt.figure(figsize=(14, 5))
    
    # Plot training data
    plt.plot(data.index[:len(train_predictions)], y_train_unscaled, label='Train Actual')
    plt.plot(data.index[time_step:len(train_predictions) + time_step], train_predictions, label='Train Predictions')
    
    # Plot testing data
    plt.plot(data.index[test_start_index:test_start_index + len(y_test_unscaled)], y_test_unscaled, label='Test Actual')
    plt.plot(data.index[test_start_index:test_start_index + len(test_predictions)], test_predictions, label='Test Predictions')
    
    plt.title(f'{ticker} Stock Price Prediction')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()
    st.pyplot(plt)