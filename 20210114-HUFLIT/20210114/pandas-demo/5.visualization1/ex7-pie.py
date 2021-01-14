import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(3 * np.random.rand(4),
                  index=['a', 'b', 'c', 'd'],
                  columns=['x'])
print(df)
df.plot.pie(subplots=True)
plt.show()