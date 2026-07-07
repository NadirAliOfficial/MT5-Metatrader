# MT5 MetaTrader Data Integration

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

## Usage

```python
from first_Milestone import connect, get_ohlcv

connect()
df = get_ohlcv("EURUSD", "H1", bars=500)
print(df.tail())
```

## Milestones

| File | Description |
|------|-------------|
| `first_Milestone.py` | MT5 connection + OHLCV fetcher |
| `second_Milestone.py` | Multi-symbol batch downloader |
| `third_final_Milestone.py` | Indicator engine + CSV export |

## Supported Timeframes

`M1` `M5` `M15` `M30` `H1` `H4` `D1` `W1` `MN1`
