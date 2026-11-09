# MT5 MetaTrader Data Integration

**Project Description**

This repository provides a Python‑based integration with MetaTrader 5 (MT5) for retrieving, processing, and analyzing historical market data. It demonstrates how to connect to the MT5 terminal, fetch OHLCV data across multiple timeframes, calculate common technical indicators using TA‑Lib, and optionally apply machine‑learning models for forecasting.

Python integration with MetaTrader 5 (MT5) to retrieve, process, and analyze historical market data (OHLCV) across multiple timeframes.

## Features

- Connect to MT5 terminal via Python API
- Fetch OHLCV data for any symbol and timeframe
- Store data in Pandas DataFrames for analysis
- Multi-timeframe support: M5, M15, H1, H4, D1
- Built-in technical indicator calculations
- Export to CSV for further processing

## Requirements

```bash
pip install MetaTrader5 pandas numpy
```

> MT5 terminal must be installed and running.

## Installation

The project dependencies are listed in **requirements.txt**. Install them with:

```bash
pip install -r requirements.txt
```

## Configuration

No environment variables are required for the current scripts. All connection parameters are handled by the MT5 API and the scripts themselves.

## Usage

### Basic data fetch (first milestone)

```python
from first_Milestone import connect, get_ohlcv

connect()
df = get_ohlcv("EURUSD", "H1", bars=500)
print(df.tail())
```

Run the script directly to see the full workflow:

```bash
python first_Milestone.py
```

### Advanced analysis (third milestone)

The `third_final_Milestone.py` script demonstrates preprocessing, LSTM model building, news sentiment analysis, and trade decision logic. Execute it with:

```bash
python third_final_Milestone.py
```

## Project Structure

- `LICENSE` – MIT license for the project.
- `README.md` – This documentation file.
- `requirements.txt` – Python package dependencies.
- `first_Milestone.py` – MT5 connection and OHLCV fetcher with indicator calculations.
- `second_Milestone.py` – Placeholder for multi‑symbol batch downloader (currently empty).
- `third_final_Milestone.py` – Indicator engine, LSTM forecasting, sentiment analysis, and trade decision logic.

## Milestones

| File | Description |
|------|-------------|
| `first_Milestone.py` | MT5 connection + OHLCV fetcher |
| `second_Milestone.py` | Multi-symbol batch downloader |
| `third_final_Milestone.py` | Indicator engine + CSV export |

## Supported Timeframes

`M1` `M5` `M15` `M30` `H1` `H4` `D1` `W1` `MN1`

## License

This project is licensed under the MIT License – see the **LICENSE** file for details.
