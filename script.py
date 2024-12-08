import MetaTrader5 as mt5
import pandas as pd
import talib

# Connect to MetaTrader 5
if not mt5.initialize():
    print("MT5 Initialization failed")
    mt5.shutdown()
else:
    print("MT5 Initialized successfully")

# Define the symbol for which you want to fetch data
symbol = "EURUSD"
num_bars = 1000  # Define the number of bars (data points) to fetch

# Function to get historical data
def get_historical_data(symbol, timeframe, num_bars):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, num_bars)
    if rates is None:
        print(f"Error: Unable to fetch data for {symbol}")
        return None
    else:
        # Convert to DataFrame
        rates_frame = pd.DataFrame(rates)
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        rates_frame.set_index('time', inplace=True)
        return rates_frame

# Fetch historical data for multiple timeframes
data_m5 = get_historical_data(symbol, mt5.TIMEFRAME_M5, num_bars)
data_m15 = get_historical_data(symbol, mt5.TIMEFRAME_M15, num_bars)
data_h1 = get_historical_data(symbol, mt5.TIMEFRAME_H1, num_bars)
data_h4 = get_historical_data(symbol, mt5.TIMEFRAME_H4, num_bars)
data_daily = get_historical_data(symbol, mt5.TIMEFRAME_D1, num_bars)

# Show the data for M5
print("M5 Data:")
print(data_m5.tail())

# Function to calculate technical indicators
def calculate_indicators(data):
    # Moving Averages
    data['SMA_50'] = talib.SMA(data['close'], timeperiod=50)
    data['SMA_200'] = talib.SMA(data['close'], timeperiod=200)
    
    # RSI (Relative Strength Index)
    data['RSI'] = talib.RSI(data['close'], timeperiod=14)
    
    # MACD (Moving Average Convergence Divergence)
    macd, macdsignal, macdhist = talib.MACD(data['close'], fastperiod=12, slowperiod=26, signalperiod=9)
    data['MACD'] = macd
    data['MACD_Signal'] = macdsignal
    data['MACD_Hist'] = macdhist
    
    # ATR (Average True Range)
    data['ATR'] = talib.ATR(data['high'], data['low'], data['close'], timeperiod=14)
    
    # Bollinger Bands
    upperband, middleband, lowerband = talib.BBANDS(data['close'], timeperiod=20, nbdevup=2, nbdevdn=2, matype=0)
    data['BB_Upper'] = upperband
    data['BB_Middle'] = middleband
    data['BB_Lower'] = lowerband

    return data

# Calculate indicators for M5 data
data_m5 = calculate_indicators(data_m5)
print("M5 Data with Indicators:")
print(data_m5[['SMA_50', 'SMA_200', 'RSI', 'MACD', 'ATR', 'BB_Upper', 'BB_Middle', 'BB_Lower']].tail())

# Calculate indicators for M15 data
data_m15 = calculate_indicators(data_m15)
print("M15 Data with Indicators:")
print(data_m15[['SMA_50', 'SMA_200', 'RSI', 'MACD', 'ATR', 'BB_Upper', 'BB_Middle', 'BB_Lower']].tail())

# Calculate indicators for H1 data
data_h1 = calculate_indicators(data_h1)
print("H1 Data with Indicators:")
print(data_h1[['SMA_50', 'SMA_200', 'RSI', 'MACD', 'ATR', 'BB_Upper', 'BB_Middle', 'BB_Lower']].tail())

# Calculate indicators for H4 data
data_h4 = calculate_indicators(data_h4)
print("H4 Data with Indicators:")
print(data_h4[['SMA_50', 'SMA_200', 'RSI', 'MACD', 'ATR', 'BB_Upper', 'BB_Middle', 'BB_Lower']].tail())

# Calculate indicators for Daily data
data_daily = calculate_indicators(data_daily)
print("Daily Data with Indicators:")
print(data_daily[['SMA_50', 'SMA_200', 'RSI', 'MACD', 'ATR', 'BB_Upper', 'BB_Middle', 'BB_Lower']].tail())

# Shutdown MT5
mt5.shutdown()
