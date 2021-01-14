import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
df = read_csv('sales-by-years-1.csv')
print(df)
# print(len(df.index))
# print(df.shape[0])
df.plot(x='years',y='sales',rot=30,title='Sales by Years', xticks=df['years'])
plt.tight_layout()
plt.show()