import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
df = read_csv('sales-by-years-22.csv')
print(df)
df[:10].plot(x='years', y= ['ABS','DXG'], rot=30)
df[:10].plot(x='years', y= ['ABS','DXG'], xticks=range(2010,2021), rot=30)
df[:10].plot(x='years', y= ['ABS','DXG'], xticks=df[:10]['years'], rot=30)
plt.title("Sales by Years")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()