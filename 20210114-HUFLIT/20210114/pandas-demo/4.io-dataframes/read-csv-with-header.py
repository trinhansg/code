# Load CSV with Pandas (CSV with header)
from pandas import read_csv
path = r"..\data\iris.csv"
df = read_csv(path)
# print dimensions of the dataframe
print(df.shape)
# print data types of the dataframe columns
print(df.dtypes)
# print the first 5 rows
print(df.head())