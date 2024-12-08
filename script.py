import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime

# Initialize MT5 connection
def initialize_mt5():
    if not mt5.initialize():
        print("Initialization failed, error code =", mt5.last_error())
        quit()
    else:
        print("Connected to MetaTrader 5")

# Fetch historical data for a specific symbol and timeframe
def fetch_data(symbol, timeframe, n=100):
    # Fetch data starting from position 0 and get 'n' bars
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n)
    
    if rates is None:
        print(f"Failed to fetch data for {symbol} on timeframe {timeframe}")
        return None
    
    # Convert to DataFrame
    df = pd.DataFrame(rates)
    # Convert time from timestamp to datetime
    df['time'] = pd.to_datetime(df['time'], unit='s')
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
            data[tf_name] = df
            print(f"Data for {tf_name}:\n", df.head())
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
        print("M5 Data Head:")
        print(data["M5"].head())
    
    # Shutdown MT5 connection
    shutdown_mt5()
