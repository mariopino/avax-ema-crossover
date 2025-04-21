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
Initial Backtest Results (n1=5, n2=10):

Start                     2020-07-13 00:00:00
End                       2025-04-19 00:00:00
Duration                   1741 days 00:00:00
Exposure Time [%]                    64.49492
Equity Final [$]                  84404.35559
Equity Peak [$]                  131397.26741
Commissions [$]                    6967.14317
Return [%]                          744.04356
Buy & Hold Return [%]               380.18035
Return (Ann.) [%]                     59.2597
Volatility (Ann.) [%]                141.9051
CAGR [%]                              56.3911
Sharpe Ratio                           0.4176
Sortino Ratio                         1.24001
Calmar Ratio                          0.92203
Alpha [%]                            688.7852
Beta                                  0.14535
Max. Drawdown [%]                   -64.27071
Avg. Drawdown [%]                   -16.65351
Max. Drawdown Duration      638 days 00:00:00
Avg. Drawdown Duration       65 days 00:00:00
# Trades                                  104
Win Rate [%]                         26.92308
Best Trade [%]                      314.00371
Worst Trade [%]                          -5.0
Avg. Trade [%]                        2.24164
Max. Trade Duration          69 days 00:00:00
Avg. Trade Duration          10 days 00:00:00
Profit Factor                         2.56922
Expectancy [%]                        5.45498
SQN                                   1.05125
Kelly Criterion                       0.10483
_strategy                            EmaCross

...

Optimized Backtest Results (n1=14, n2=38):

Start                     2020-07-13 00:00:00
End                       2025-04-19 00:00:00
Duration                   1741 days 00:00:00
Exposure Time [%]                    68.97788
Equity Final [$]                3301035.45956
Equity Peak [$]                 5042526.73749
Commissions [$]                   64678.88646
Return [%]                         32910.3546
Buy & Hold Return [%]               382.59254
Return (Ann.) [%]                   254.40212
Volatility (Ann.) [%]               422.85805
CAGR [%]                            237.31377
Sharpe Ratio                          0.60163
Sortino Ratio                         5.23682
Calmar Ratio                           4.1724
Alpha [%]                         32783.84958
Beta                                  0.33065
Max. Drawdown [%]                   -60.97254
Avg. Drawdown [%]                   -11.14603
Max. Drawdown Duration      323 days 00:00:00
Avg. Drawdown Duration       32 days 00:00:00
# Trades                                   34
Win Rate [%]                         38.23529
Best Trade [%]                      498.34658
Worst Trade [%]                          -5.0
Avg. Trade [%]                        18.8293
Max. Trade Duration         128 days 00:00:00
Avg. Trade Duration          34 days 00:00:00
Profit Factor                        13.78641
Expectancy [%]                       39.48743
SQN                                   1.94721
Kelly Criterion                        0.2969
_strategy                 EmaCross(n1=14,n...
_equity_curve                             ...
_trades                         Size  Entr...
dtype: object

Best Run Trades:

     Type  EntryTime   ExitTime  EntryPrice   ExitPrice           PnL   ReturnPct Duration
0    Long 2020-11-24 2020-11-25    4.266966    4.053618 -4.994484e+02   -5.000000   1 days
1   Short 2020-11-26 2020-11-27    3.527710    3.704095 -4.734187e+02   -5.000000   1 days
2    Long 2021-01-05 2021-04-22    4.237412   24.034962  4.195101e+04  467.208519 107 days
3   Short 2021-04-22 2021-04-26   24.034962   25.236710 -2.540495e+03   -5.000000   4 days
4    Long 2021-05-03 2021-05-04   35.932320   34.135704 -2.409262e+03   -5.000000   1 days
5   Short 2021-05-21 2021-08-06   21.801769   14.725431  1.482493e+04   32.457631  77 days
6    Long 2021-08-06 2021-12-12   14.725431   88.109116  3.010933e+05  498.346581 128 days
7   Short 2021-12-12 2021-12-15   88.109116   92.514571 -1.803594e+04   -5.000000   3 days
8    Long 2021-12-17 2021-12-20  111.008766  105.458328 -1.710090e+04   -5.000000   3 days
9   Short 2022-01-07 2022-01-09   86.767715   91.106101 -1.621255e+04   -5.000000   2 days
10   Long 2022-02-16 2022-02-17   95.346115   90.578809 -1.536979e+04   -5.000000   1 days
11  Short 2022-02-21 2022-02-22   69.988930   73.488376 -1.457170e+04   -5.000000   1 days
12   Long 2022-03-20 2022-04-11   84.724304   80.488089 -1.381430e+04   -5.000000  22 days
13  Short 2022-04-13 2022-07-22   80.001976   23.715851  1.842808e+05   70.355919 100 days
14   Long 2022-07-22 2022-07-25   23.715851   22.530058 -2.228579e+04   -5.000000   3 days
15  Short 2022-08-25 2022-10-31   23.020317   19.311609  6.808075e+04   16.110585  67 days
16   Long 2022-10-31 2022-11-02   19.311609   18.346029 -2.449195e+04   -5.000000   2 days
17  Short 2022-11-09 2022-11-10   12.917875   13.563769 -2.322053e+04   -5.000000   1 days
18   Long 2023-01-12 2023-03-03   15.457350   16.654383  3.409389e+04    7.744102  50 days
19  Short 2023-03-03 2023-03-14   16.654383   17.487102 -2.367004e+04   -5.000000  11 days
20   Long 2023-04-01 2023-04-03   17.662683   16.779549 -2.243956e+04   -5.000000   2 days
21  Short 2023-04-28 2023-07-14   17.563816   14.644426  7.072514e+04   16.621614  77 days
22   Long 2023-07-14 2023-07-18   14.644426   13.912205 -2.476885e+04   -5.000000   4 days
23  Short 2023-07-28 2023-10-24   13.238449   10.314807  1.037250e+05   22.084476  88 days
24   Long 2023-10-24 2024-01-20   10.314807   32.808426  1.248351e+06  218.071158  88 days
25  Short 2024-01-20 2024-01-28   32.808426   34.448847 -9.085801e+04   -5.000000   8 days
26   Long 2024-02-08 2024-04-11   35.427765   46.057598  5.168756e+05   30.004245  63 days
27  Short 2024-04-11 2024-07-23   46.057598   29.841068  7.869558e+05   35.209239 103 days
28   Long 2024-07-23 2024-07-24   29.841068   28.349015 -1.508779e+05   -5.000000   1 days
29  Short 2024-07-24 2024-09-14   28.396355   25.330502  3.088878e+05   10.796643  52 days
30   Long 2024-09-14 2024-09-15   25.330502   24.063976 -1.582067e+05   -5.000000   1 days
31  Short 2024-10-30 2024-11-07   26.198242   27.508154 -1.499954e+05   -5.000000   8 days
32   Long 2024-11-09 2024-12-26   30.417948   37.280796  6.416420e+05   22.561839  47 days
33  Short 2024-12-26 2025-01-02   37.280796   39.144836 -1.739298e+05   -5.000000   7 days
```