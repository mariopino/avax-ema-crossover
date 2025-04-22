# Backtesting the EMA crossover strategy on the AVAX-USD pair

Backtesting the EMA crossover strategy on the [AVAX-USD](https://finance.yahoo.com/quote/AVAX-USD/) pair using [Backtesting.py](https://kernc.github.io/backtesting.py/) Python library.

The script does the following:

- Download daily OHLCV data from Yahoo Finance
- Initial run with predefined parameters
- Optimization
- Run with optimized parameters
- Generates a candle chart with indicators and trades (EmaCross_n1-XX,n2-YY_.html)
- Generates a Heatmap for the different combination of slow and fast moving averages (EmaCross.html)
- Export trades to CSV file (trades.csv)

The best results were achieved using a 5% stop loss for both SHORT and LONG trades.

# Installation

## Clone repository:

```
git clone https://github.com/mariopino/avax-ema-crossover.git
cd avax-ema-crossover
```

## Create virtual environment

### VSCode

To create local environments in VS Code using virtual environments or Anaconda, you can follow these steps: open the Command Palette (Ctrl+Shift+P), search for the Python: Create Environment command, and select it, then select Venv.

Select and activate an environment

Use the `Python: Select Interpreter` command from the Command Palette (Ctrl+Shift+P) and then select `.\.venv\Scripts\python.exe`.

### Linux

```
python -m venv myvenv
source myvenv/bin/activate
```

## Install dependencies

```
pip install backtesting
pip install yfinance
```

# Execute script

## Windows

```
python.exe EmaCross.py
```

## Linux

```
python EmaCross.py
```

# Results:

```
Initial Backtest Results (n1=40, n2=170):

Start                     2025-03-24 00:00...
End                       2025-04-22 08:30...
Duration                     29 days 08:30:00
Exposure Time [%]                    75.74468
Equity Final [$]                   12657.9315
Equity Peak [$]                   13179.34361
Commissions [$]                      66.77907
Return [%]                           26.57932
Buy & Hold Return [%]                -7.77331
Return (Ann.) [%]                  1659.59756
Volatility (Ann.) [%]              1313.12229
CAGR [%]                           1774.19257
Sharpe Ratio                          1.26386
Sortino Ratio                        45.82157
Calmar Ratio                        110.75646
Alpha [%]                            24.59642
Beta                                 -0.25509
Max. Drawdown [%]                   -14.98421
Avg. Drawdown [%]                    -1.53869
Max. Drawdown Duration       15 days 02:00:00
Avg. Drawdown Duration        0 days 16:22:00
# Trades                                    3
Win Rate [%]                         66.66667
Best Trade [%]                       16.26755
Worst Trade [%]                      -0.61527
Avg. Trade [%]                        6.99323
Max. Trade Duration          12 days 16:00:00
Avg. Trade Duration           7 days 09:50:00
Profit Factor                        36.18537
Expectancy [%]                        7.21619
SQN                                   1.52236
Kelly Criterion                       0.64496
_strategy                            EmaCross

...

Optimized Backtest Results (n1=40, n2=170):

Start                     2025-03-24 00:00...
End                       2025-04-22 08:30...
Duration                     29 days 08:30:00
Exposure Time [%]                    75.74468
Equity Final [$]                   12657.9315
Equity Peak [$]                   13179.34361
Commissions [$]                      66.77907
Return [%]                           26.57932
Buy & Hold Return [%]                -7.77331
Return (Ann.) [%]                  1659.59756
Volatility (Ann.) [%]              1313.12229
CAGR [%]                           1774.19257
Sharpe Ratio                          1.26386
Sortino Ratio                        45.82157
Calmar Ratio                        110.75646
Alpha [%]                            24.59642
Beta                                 -0.25509
Max. Drawdown [%]                   -14.98421
Avg. Drawdown [%]                    -1.53869
Max. Drawdown Duration       15 days 02:00:00
Avg. Drawdown Duration        0 days 16:22:00
# Trades                                    3
Win Rate [%]                         66.66667
Best Trade [%]                       16.26755
Worst Trade [%]                      -0.61527
Avg. Trade [%]                        6.99323
Max. Trade Duration          12 days 16:00:00
Avg. Trade Duration           7 days 09:50:00
Profit Factor                        36.18537
Expectancy [%]                        7.21619
SQN                                   1.52236
Kelly Criterion                       0.64496
_strategy                 EmaCross(n1=40,n...
_equity_curve                             ...
_trades                      Size  EntryBa...
dtype: object

Best Run Trades:

    Type                 EntryTime                  ExitTime  EntryPrice  ExitPrice          PnL  ReturnPct         Duration
0  Short 2025-03-28 02:30:00+00:00 2025-04-09 18:30:00+00:00   21.821156  18.271387  1622.244181  16.267555 12 days 16:00:00
1   Long 2025-04-09 18:30:00+00:00 2025-04-15 21:30:00+00:00   18.271387  19.366993   694.614109   5.996293  6 days 03:00:00
2  Short 2025-04-15 21:30:00+00:00 2025-04-19 08:00:00+00:00   19.366993  19.486153   -75.428089  -0.615272  3 days 10:30:00
```