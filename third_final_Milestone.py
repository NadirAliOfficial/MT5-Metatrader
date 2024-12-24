import MetaTrader5 as mt5
import pandas as pd
import numpy as np
import talib
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
from datetime import datetime
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# Initialize MetaTrader5 connection
if not mt5.initialize():
    print("MT5 Initialization failed")
    mt5.shutdown()
else:
    print("MT5 Initialized successfully")

# Function to fetch historical data
def get_historical_data(symbol, timeframe, num_bars):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_bars)
    if rates is None:
        print(f"Error: Unable to fetch data for {symbol}")
        return None
    else:
        rates_frame = pd.DataFrame(rates)
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        rates_frame.set_index('time', inplace=True)
        return rates_frame

# Preprocess data for LSTM
def preprocess_data(data, feature_col='close', look_back=60):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data[feature_col].values.reshape(-1, 1))

    x, y = [], []
    for i in range(look_back, len(scaled_data)):
        x.append(scaled_data[i - look_back:i, 0])
        y.append(scaled_data[i, 0])
    
    x, y = np.array(x), np.array(y)
    x = np.reshape(x, (x.shape[0], x.shape[1], 1))
    return x, y, scaler

# Build LSTM model
# Build LSTM model
def build_lstm(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(input_shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=False))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))  # Predicting one value
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Export model architecture and weights
def export_model(model):
    # Save model architecture to JSON
    model_json = model.to_json()
    with open("lstm_model_architecture.json", "w") as json_file:
        json_file.write(model_json)

    # Save model weights
    model.save_weights("lstm_model_weights.h5")
    print("Model architecture and weights exported successfully!")

# Predict future trends with LSTM
def predict_with_lstm(model, data, scaler, look_back=60):
    # Ensure data is reshaped for LSTM input
    last_data = data[-look_back:].reshape(1, look_back, 1)  # Reshape to (1, look_back, 1)
    scaled_prediction = model.predict(last_data)  # Predict scaled value
    return scaler.inverse_transform(scaled_prediction)[0][0]  # Inverse scale prediction

    return scaler.inverse_transform(prediction)[0][0]

# Fetch news and analyze sentiment
def fetch_news():
    url = "https://newsapi.org/v2/everything"
    params = {
        'q': 'forex',  
        'apiKey': '2747a6ae0aa149dfac5e738a93667e17',
        'language': 'en',
        'pageSize': 5  
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        headlines = [article['title'] for article in data['articles']]
        return headlines
    else:
        print(f"Error: Unable to fetch news (status code {response.status_code})")
        return []

# Sentiment analysis
def analyze_sentiment(news_headlines):
    analyzer = SentimentIntensityAnalyzer()
    sentiments = [analyzer.polarity_scores(headline)['compound'] for headline in news_headlines]
    return sentiments

# Decide whether to trade
def should_trade(sentiments, prediction):
    positive_sentiments = [score for score in sentiments if score > 0]
    if positive_sentiments and prediction > 1.01:  # Example threshold for prediction
        return "Positive sentiment and upward trend detected. Trade will be executed."
    else:
        return "No favorable conditions. Trade will not be executed."

# Function to place a buy order
def place_buy_order(symbol, lot_size=0.1):
    price = mt5.symbol_info_tick(symbol).ask
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": mt5.ORDER_TYPE_BUY,
        "price": price,
        "sl": price - 50 * mt5.symbol_info(symbol).point,
        "tp": price + 50 * mt5.symbol_info(symbol).point,
        "deviation": 10,
        "magic": 234000,
        "comment": "LSTM-based Buy Order",
        "type_filling": mt5.ORDER_FILLING_IOC,
        "type_time": mt5.ORDER_TIME_GTC
    }
    result = mt5.order_send(request)
    return result

# Function to place a sell order
def place_sell_order(symbol, lot_size=0.1):
    price = mt5.symbol_info_tick(symbol).bid
    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": lot_size,
        "type": mt5.ORDER_TYPE_SELL,
        "price": price,
        "sl": price + 50 * mt5.symbol_info(symbol).point,
        "tp": price - 50 * mt5.symbol_info(symbol).point,
        "deviation": 10,
        "magic": 234000,
        "comment": "LSTM-based Sell Order",
        "type_filling": mt5.ORDER_FILLING_IOC,
        "type_time": mt5.ORDER_TIME_GTC
    }
    result = mt5.order_send(request)
    return result

# Main function
def main():
    symbol = "EURUSD"
    timeframe = mt5.TIMEFRAME_M5
    num_bars = 1000

    # Step 1: Fetch historical data
    data = get_historical_data(symbol, timeframe, num_bars)
    if data is None:
        return

    # Step 2: Preprocess data for LSTM
    x, y, scaler = preprocess_data(data)

    # Step 3: Build and train LSTM
    model = build_lstm(x.shape)
    model.fit(x, y, epochs=5, batch_size=32, verbose=1)

    # Step 4: Predict future trends
    prediction = predict_with_lstm(model, x, scaler)
    print(f"LSTM Prediction: {prediction}")
    
    # Step 5: Export model architecture and weights
    export_model(model)

    # Step 6: Fetch and analyze news
    news = fetch_news()
    sentiments = analyze_sentiment(news)

    # Step 7: Final decision
    decision = should_trade(sentiments, prediction)
    print(decision)

    # Step 8: Place trade based on decision
    if "Trade will be executed" in decision:
        # Example of placing a buy order
        result = place_buy_order(symbol)
        print(f"Buy Order Result: {result}")
    else:
        print("No trade executed.")

# Run main function
main()

# Shutdown MT5
mt5.shutdown()
