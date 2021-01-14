from pandas import read_csv
path = r"output1.csv"
data = read_csv(path, index_col = 0)
print(data.head())