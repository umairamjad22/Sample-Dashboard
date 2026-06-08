# PSX stocks via yfinance — use .KA suffix
import yfinance as yf
import pandas as pd

psx_tickers = ['ENGRO.KA', 'HBL.KA', 'OGDC.KA',
               'LUCK.KA', 'SYS.KA']

data = yf.download(psx_tickers,
                  start='2022-01-01',
                  end='2025-01-01',
                  auto_adjust=True)

close = data['Close'] # prices in PKR
returns = close.pct_change().dropna()
print(returns.describe())
