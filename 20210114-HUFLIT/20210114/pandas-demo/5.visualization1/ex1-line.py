# This functionality on Series and DataFrame
# is just a simple wrapper around the matplotlib libraries plot() method.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),
                  index=pd.date_range('1/1/2000',periods=10),
                  columns=list('ABCD'))
print(df)
df.plot()
plt.show()
