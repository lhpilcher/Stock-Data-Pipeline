import os
import pandas as pd
import sqlite3
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

os.makedirs("data", exist_ok=True)
os.makedirs("db", exist_ok=True)


tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"]

data_frames = []
for ticker in tickers:
    print(f"Fetching data for {ticker}...")
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    hist['Ticker'] = ticker
    hist.reset_index(inplace=True)
    data_frames.append(hist)

df = pd.concat(data_frames, ignore_index=True)
print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

db_file = "db/stock_data.db"
conn = sqlite3.connect(db_file)
df.to_sql("stock_prices", conn, if_exists="replace", index=False)
print(f"Data saved to database: {db_file}")


query = """
SELECT Ticker, AVG(Close) as avg_close
FROM stock_prices
GROUP BY Ticker
ORDER BY avg_close DESC
"""
avg_close = pd.read_sql_query(query, conn)
print("Average closing price per stock:")
print(avg_close)

# Step 5: Optional visualization - Close price trends
plt.figure(figsize=(10,5))
for ticker in tickers:
    stock_data = df[df['Ticker'] == ticker]
    plt.plot(stock_data['Date'], stock_data['Close'], label=ticker)
plt.title("Stock Closing Prices Last Month")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.xticks(rotation=30)
plt.show()

conn.close()
