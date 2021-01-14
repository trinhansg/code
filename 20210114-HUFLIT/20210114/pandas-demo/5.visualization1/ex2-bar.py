import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
print(df)
df.plot.bar()
# df.plot.bar(stacked=True)
# df.plot.barh(stacked=True)
plt.show()