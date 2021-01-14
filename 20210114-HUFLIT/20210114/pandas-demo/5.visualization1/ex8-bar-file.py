import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
path = r"..\data\iris.csv"
df = read_csv(path)[:6]
print(df)
df[['sepal_length', 'sepal_width']].plot.bar()
# df.plot.bar(stacked=True)
# df.plot.barh(stacked=True)
plt.show()