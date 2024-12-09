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
MT5 Initialized successfully
M5 Data:
                        open     high      low    close  tick_volume  spread  real_volume
time
2024-12-09 06:50:00  1.05346  1.05363  1.05342  1.05357          104       4            0
2024-12-09 06:55:00  1.05357  1.05357  1.05338  1.05346           94       4            0
2024-12-09 07:00:00  1.05346  1.05361  1.05342  1.05358          105       4            0
2024-12-09 07:05:00  1.05357  1.05367  1.05354  1.05362           85       4            0
2024-12-09 07:10:00  1.05361  1.05368  1.05357  1.05367           28       4            0
M5 Data with Indicators:
                       SMA_50   SMA_200        RSI      MACD       ATR  BB_Upper  BB_Middle  BB_Lower
time
2024-12-09 06:50:00  1.054864  1.056118  33.521331 -0.000452  0.000255  1.055172   1.054004  1.052836
2024-12-09 06:55:00  1.054821  1.056093  31.619751 -0.000437  0.000251  1.054938   1.053912  1.052886
2024-12-09 07:00:00  1.054775  1.056069  35.892205 -0.000411  0.000246  1.054724   1.053837  1.052951
2024-12-09 07:05:00  1.054729  1.056045  37.298536 -0.000382  0.000238  1.054593   1.053786  1.052979
2024-12-09 07:10:00  1.054686  1.056021  39.097035 -0.000352  0.000229  1.054408   1.053732  1.053056
M15 Data with Indicators:
                       SMA_50   SMA_200        RSI      MACD       ATR  BB_Upper  BB_Middle  BB_Lower
time
2024-12-09 06:00:00  1.055703  1.056086  31.269350 -0.000502  0.000550  1.056851   1.055382  1.053913
2024-12-09 06:15:00  1.055643  1.056094  26.854715 -0.000585  0.000559  1.056902   1.055236  1.053570
2024-12-09 06:30:00  1.055585  1.056100  28.605503 -0.000635  0.000541  1.056848   1.055089  1.053330
2024-12-09 06:45:00  1.055513  1.056108  29.334125 -0.000664  0.000526  1.056696   1.054935  1.053173
2024-12-09 07:00:00  1.055446  1.056115  33.189157 -0.000662  0.000507  1.056583   1.054816  1.053049
H1 Data with Indicators:
                       SMA_50   SMA_200        RSI      MACD       ATR  BB_Upper  BB_Middle  BB_Lower
time
2024-12-09 03:00:00  1.056044  1.053462  42.611625 -0.000218  0.001473  1.059795   1.056993  1.054191
2024-12-09 04:00:00  1.056125  1.053508  44.447956 -0.000266  0.001408  1.059765   1.056895  1.054025
2024-12-09 05:00:00  1.056175  1.053540  36.796295 -0.000440  0.001448  1.059763   1.056663  1.053563
2024-12-09 06:00:00  1.056205  1.053567  35.809952 -0.000592  0.001400  1.059739   1.056426  1.053114
2024-12-09 07:00:00  1.056233  1.053595  37.272507 -0.000688  0.001319  1.059687   1.056224  1.052761
H4 Data with Indicators:
                       SMA_50   SMA_200        RSI      MACD       ATR  BB_Upper  BB_Middle  BB_Lower
time
2024-12-06 12:00:00  1.053170  1.065768  66.055293  0.001722  0.003251  1.060158   1.053669  1.047180
2024-12-06 16:00:00  1.053257  1.065630  51.731391  0.001520  0.003467  1.060294   1.053822  1.047350
2024-12-06 20:00:00  1.053383  1.065507  54.814048  0.001469  0.003414  1.060584   1.054035  1.047487
2024-12-09 00:00:00  1.053546  1.065379  51.477804  0.001295  0.003299  1.060695   1.054152  1.047609
2024-12-09 04:00:00  1.053658  1.065248  48.230436  0.001023  0.003236  1.060642   1.054311  1.047980
Daily Data with Indicators:
              SMA_50   SMA_200        RSI      MACD       ATR  BB_Upper  BB_Middle  BB_Lower
time
2024-12-03  1.078560  1.084726  39.400495 -0.008047  0.008692  1.075655   1.057172  1.038689
2024-12-04  1.077308  1.084561  39.515137 -0.007737  0.008583  1.073344   1.056075  1.038806
2024-12-05  1.076121  1.084450  47.012906 -0.006797  0.008573  1.068256   1.054970  1.041684
2024-12-06  1.074929  1.084314  45.742070 -0.006109  0.008585  1.065085   1.054213  1.043341
2024-12-09  1.073735  1.084156  43.435821 -0.005732  0.008237  1.063305   1.053646  1.043987
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
