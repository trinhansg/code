from pandas import read_csv

df = read_csv('sales-by-years-2.csv')
df = df.pivot(index='tickers',columns='years',values='sales')
print(df)
df=df.reset_index()
print(df)
