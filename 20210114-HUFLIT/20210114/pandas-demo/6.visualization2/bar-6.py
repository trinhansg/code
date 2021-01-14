import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
from mylib.viz import autolabel

df = read_csv('sales-by-years-22.csv')
print(df)
ax = df.plot.bar(x='years',y=['ABS','DXG'], figsize=(12,6))
autolabel(ax, ax.patches)
plt.title("Sales by Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


