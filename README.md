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
   git clone https://github.com/NadirAliOfficial/MT5-Metatrader.git
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
   python script.py
   ```

   The script will output the first few rows of data for each timeframe.

### **Output**:
```bash
Fetching data for Daily timeframe...
Data for Daily:
         time     open     high      low    close  tick_volume  spread  real_volume
0 2024-07-22  1.08880  1.09025  1.08731  1.08902        34953       0            0
1 2024-07-23  1.08887  1.08967  1.08437  1.08530        33815       0            0
2 2024-07-24  1.08514  1.08665  1.08257  1.08393        37830       0            0
3 2024-07-25  1.08392  1.08699  1.08282  1.08446        45357       0            0
4 2024-07-26  1.08448  1.08682  1.08421  1.08552        34860       0            0
M5 Data Head:
                 time     open     high      low    close  tick_volume  spread  real_volume
0 2024-12-06 15:40:00  1.06216  1.06238  1.06144  1.06168          479       4            0
1 2024-12-06 15:45:00  1.06169  1.06177  1.05958  1.05989          424       3            0
2 2024-12-06 15:50:00  1.05994  1.06130  1.05989  1.06113          419       4            0
3 2024-12-06 15:55:00  1.06115  1.06116  1.05982  1.06043          388       3            0
4 2024-12-06 16:00:00  1.06046  1.06069  1.05912  1.05917          376       4            0
MT5 connection closed
...
```

### **File Structure**
```
├── script.py                  # Main script for MT5 data retrieval
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
This project is licensed under the MIT License.

---

### **MT5 Integration & Data Retrieval**
This repository contains a Python script for integrating with MetaTrader 5 (MT5) and retrieving historical market data (OHLC and volume) for multiple timeframes. The data is retrieved and stored in Pandas DataFrames for further processing and analysis. This project is intended to serve as a base for algorithmic trading, backtesting strategies, and conducting technical analysis.
