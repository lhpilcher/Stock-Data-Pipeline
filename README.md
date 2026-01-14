# Stock Data Pipeline

![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

Python ETL pipeline that fetches real-time stock data, stores it in SQLite, performs analytics, and visualizes trends.
---

## Features

- Fetches live stock data for multiple tickers (AAPL, MSFT, GOOG, AMZN, TSLA) using Yahoo Finance API
- Transforms and stores data in SQLite
- Performs SQL analytics: average close price per stock
- Optional visualization with matplotlib: trends over the last month
- Fully reproducible pipeline

---

## Requirements

- Python 3.8+
- pandas
- yfinance
- matplotlib
- sqlite3 (built-in)

Install dependencies:

```bash
pip install -r requirements.txt
