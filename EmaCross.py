from backtesting import Backtest, Strategy
from backtesting.lib import crossover, plot_heatmaps
import yfinance as yf
import numpy as np
import pandas as pd
import pandas_ta as ta

#
# Set up parameters
#

ticker_name = "AVAX-USD"  # Ticker name for AVAX-USD
cash = 10000  # Initial cash amount in USD
commission = 0.001  # Commission per trade
exclusive_orders = True  # Only one order at a time
period = '30d'  # Period for data download
interval = '30m'  # Interval for data download
n1 = 40  # Fast EMA
n2 = 170 # Slow EMA

# Download and prepare data from Yahoo Finance
data = yf.download(ticker_name, period=period, interval=interval)
data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
data.columns = ['Open', 'High', 'Low', 'Close', 'Volume']

# Uncomment the following line to see the data before running the backtest
# print(data.tail())

class EmaCross(Strategy):
    n1 = n1
    n2 = n2

    def init(self):
        close = pd.Series(self.data.Close, index=self.data.index)
        self.ema1 = self.I(ta.ema, close, self.n1)
        self.ema2 = self.I(ta.ema, close, self.n2)

    def next(self):
        if crossover(self.ema1, self.ema2):
            # LONG: If the fast EMA crosses above the slow EMA
            if self.position.is_short:
                self.position.close()
            self.buy(sl=self.data.Close[-1] * 0.95)
        elif crossover(self.ema2, self.ema1):
            # SHORT: If the fast EMA crosses below the slow EMA
            if self.position.is_long:
                self.position.close()
            self.sell(sl=self.data.Close[-1] * 1.05)

# Initialize the backtest
bt = Backtest(
    data,
    EmaCross,
    cash=cash,
    commission=commission,
    exclusive_orders=exclusive_orders,
    trade_on_close=True # Use close price for trades, could be dangerous if there's a big gap between close and open (e.g. weekends)
)

# Print results of the backtest
print(f"\nInitial Backtest Results (n1={n1}, n2={n2}):\n")
print(bt.run())

# Run optimization
optimization_results, heatmap = bt.optimize(
    n1=range(2, 52, 2),  # Fast EMA from 2 to 50, step 2
    n2=range(10, 202, 2),  # Slow EMA from 10 to 200, step 2
    maximize='Return [%]',  # Maximize Sortino Ratio
    constraint=lambda p: p.n1 < p.n2,  # Ensure fast EMA is shorter than slow EMA
    return_heatmap=True # Return heatmap data
)

# Print optimization results
best_n1 = optimization_results._strategy.n1
best_n2 = optimization_results._strategy.n2
print(f"\nOptimized Backtest Results (n1={best_n1}, n2={best_n2}):\n")
print(optimization_results)

# Run the backtest with the best parameters
best_run = bt.run(n1=best_n1, n2=best_n2)

# Plot the results of the best run
bt.plot()

# Copy the trades DataFrame
trades = best_run['_trades'].copy()

# Add the trade type
trades['Type'] = np.where(trades['Size'] > 0, 'Long', 'Short')

# Compute return in percentage
trades['ReturnPct'] = np.where(
    trades['Type'] == 'Long',
    (trades['ExitPrice'] - trades['EntryPrice']) / trades['EntryPrice'] * 100,
    (trades['EntryPrice'] - trades['ExitPrice']) / trades['EntryPrice'] * 100
)

# Cleanup and reorder columns
useful_cols = ['Type', 'EntryTime', 'ExitTime', 'EntryPrice', 'ExitPrice', 'PnL', 'ReturnPct', 'Duration']
trades = trades[useful_cols]

# Print the trades
print("\nBest Run Trades:\n")
print(trades.to_string())

# Save trades to a CSV file
trades.to_csv('trades.csv', index=False)

# Plot Heatmap
plot_heatmaps(heatmap, agg='mean')