import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv

def autolabel(ax, rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


df = read_csv('sales-by-years-1.csv')
print(df)
ax = df.plot.bar(x='years',y='sales')
# df.plot.bar(x='years', y='sales', color='red')
# ax = df.plot.bar(x='years', y='sales', color=np.random.rand(11,3), rot=30)
autolabel(ax, ax.patches)
plt.title("Sales by Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()


