## **MT5 Integration & Data Retrieval**

### **Description**
This Python project integrates with MetaTrader 5 (MT5) to retrieve historical market data (OHLC and volume) for various timeframes (M5, M15, H1, H4, Daily). The data is then stored in Pandas DataFrames for further processing and analysis. This project serves as the foundation for developing trading strategies and performing technical analysis.

### **Features**
- Connect to MetaTrader 5 (MT5) using the MetaTrader5 Python API.
- Fetch historical market data (OHLC and volume) for multiple timeframes (M5, M15, H1, H4, Daily).
- Data is stored in Pandas DataFrames for easy manipulation.
- Time conversion from Unix timestamps to human-readable datetime format.

### **Technologies Used**
- **MetaTrader5 API**: For connection to MetaTrader 5.
- **Pandas**: For data manipulation and storage.
- **Python**: The programming language used.

### **Installation**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/mt5-data-retrieval.git
   ```

2. **Install dependencies**:
   Install the required Python packages by running the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Install MetaTrader 5**:
   Make sure you have MetaTrader 5 installed and set up with a broker account to access real-time and historical data.

4. **Install the MetaTrader5 Python package**:
   You can install the MetaTrader5 Python package using:
   ```bash
   pip install MetaTrader5
   ```

### **Usage**

1. **Initialize MT5 Connection**:
   The script connects to your MetaTrader 5 terminal using your broker’s credentials. Make sure MT5 is open and running before executing the script.

2. **Fetching Data**:
   The script fetches historical data for a specified symbol (e.g., EURUSD) and stores it in a Pandas DataFrame. The script supports fetching data for different timeframes such as M5, M15, H1, H4, and Daily.

3. **Run the Script**:
   To run the script and fetch data, simply run the following command:
   ```bash
   python mt5_data_retrieval.py
   ```

   The script will output the first few rows of data for each timeframe.

### **Example Output**:
```bash
Connected to MetaTrader 5
Fetching data for M5 timeframe...
Data for M5:
                  time        open        high         low       close     volume
0 2024-12-08 00:00:00  1.069900  1.070100  1.069800  1.069900   12345
1 2024-12-08 00:05:00  1.069900  1.070200  1.069700  1.070000   12456
...
```

### **File Structure**
```
├── mt5_data_retrieval.py      # Main script for MT5 data retrieval
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
└── data                       # Folder to store historical data (optional)
```

### **Requirements**
- Python 3.x
- MetaTrader 5 terminal installed and running
- MetaTrader5 Python package
- Pandas library

### **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Repository Description for GitHub**:

### **MT5 Integration & Data Retrieval**
This repository contains a Python script for integrating with MetaTrader 5 (MT5) and retrieving historical market data (OHLC and volume) for multiple timeframes. The data is retrieved and stored in Pandas DataFrames for further processing and analysis. This project is intended to serve as a base for algorithmic trading, backtesting strategies, and conducting technical analysis.
