import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ── Plot aesthetics ────────────────────────────────────────────────────────
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams.update({
    'figure.figsize'  : (15, 6),
    'font.size'       : 12,
    'axes.titlesize'  : 14,
    'axes.titleweight': 'bold',
    'axes.labelsize'  : 12,
    'legend.fontsize' : 10,
})

print("✅ All libraries imported successfully!")
