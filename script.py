import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import pandas_ta as ta  # Import technical analysis library

# Initialize MT5 connection
def initialize_mt5():
    if not mt5.initialize():
        print("Initialization failed, error code =", mt5.last_error())
        quit()
    else:
        print("Connected to MetaTrader 5")

# Fetch historical data for a specific symbol and timeframe
def fetch_data(symbol, timeframe, n=100):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n)
    if rates is None:
        print(f"Failed to fetch data for {symbol} on timeframe {timeframe}")
        return None
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

# Add technical indicators to the data
def add_technical_indicators(df):
    if df is not None:
        # Moving Averages
        df['SMA_20'] = ta.sma(df['close'], length=20)
        df['EMA_20'] = ta.ema(df['close'], length=20)

        # RSI
        df['RSI_14'] = ta.rsi(df['close'], length=14)

        # MACD
        macd = ta.macd(df['close'], fast=12, slow=26, signal=9)
        df['MACD'] = macd['MACD_12_26_9']
        df['Signal_Line'] = macd['MACDs_12_26_9']

        # ATR
        df['ATR_14'] = ta.atr(df['high'], df['low'], df['close'], length=14)

        # Bollinger Bands
        bb = ta.bbands(df['close'], length=20, std=2)
        df['BBL'] = bb['BBL_20_2.0']
        df['BBM'] = bb['BBM_20_2.0']
        df['BBU'] = bb['BBU_20_2.0']
        df['BB_Width'] = bb['BBW_20_2.0']
    return df

# Main function to fetch data for multiple timeframes
def fetch_data_for_multiple_timeframes(symbol):
    timeframes = {
        "M5": mt5.TIMEFRAME_M5,
        "M15": mt5.TIMEFRAME_M15,
        "H1": mt5.TIMEFRAME_H1,
        "H4": mt5.TIMEFRAME_H4,
        "Daily": mt5.TIMEFRAME_D1
    }

    data = {}

    for tf_name, tf_code in timeframes.items():
        print(f"Fetching data for {tf_name} timeframe...")
        df = fetch_data(symbol, tf_code)
        if df is not None:
            df = add_technical_indicators(df)
            data[tf_name] = df
            print(f"Data for {tf_name} with Indicators:\n", df.head())
        else:
            print(f"Failed to retrieve {tf_name} data.")

    return data

# Disconnect from MT5
def shutdown_mt5():
    mt5.shutdown()
    print("MT5 connection closed")

# Main script
if __name__ == "__main__":
    symbol = "EURUSD"  # Replace with your desired symbol

    # Initialize MT5 connection
    initialize_mt5()

    # Fetch data for multiple timeframes
    data = fetch_data_for_multiple_timeframes(symbol)

    # Example: Accessing the data for M5 timeframe
    if "M5" in data:
        print("M5 Data Head with Indicators:")
        print(data["M5"].head())
    
    # Shutdown MT5 connection
    shutdown_mt5()
