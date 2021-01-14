import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
from mylib.viz import autolabel

df = read_csv('sales-by-years-1.csv')
print(df)
# df.plot.bar(x='years',y='sales')
# df.plot.bar(x='years', y='sales', color='red')
ax = df.plot.bar(x='years', y='sales', color=np.random.rand(11,3), rot=30)
autolabel(ax, ax.patches)
plt.title("Sales by Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


