import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame({'a':np.random.randn(1000) + 1,
                   'b':np.random.randn(1000),
                   'c':np.random.randn(1000) - 1},
                  columns=['a', 'b', 'c'])

df.hist(bins=20)
plt.show()