# Load CSV with Pandas (CSV without header)
from pandas import read_csv
path = r"..\data\pima-indians-diabetes.csv"
headers = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
df = read_csv(path, names=headers, comment='#')
print(df.head(10))
print(df.shape)