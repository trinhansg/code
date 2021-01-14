from pandas import read_csv
path = r"output2.csv"
df = read_csv(path, index_col = 0)
print(df.head())