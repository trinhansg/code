import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
from mylib.viz import autolabel

df = read_csv('sales-by-years-21.csv')
print(df)
df = df[df.tickers.isin(['ABS','DXG'])]
print(df)
ax = df.plot.bar(x='tickers')
# ax = df.plot.bar(x='tickers',y=['2019','2020'])
autolabel(ax, ax.patches)
plt.title("Sales by Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


