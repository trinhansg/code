import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
path = r"..\data\iris.csv"
df = read_csv(path)
print(df)
# df['sepal_length'].plot()
# df[['sepal_length', 'sepal_width']].plot()
# df.plot()
df.plot(subplots=True, layout=(2,2))
plt.show()