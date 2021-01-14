from pandas import read_csv

df = read_csv('sales-by-years-2.csv')
df = df.pivot(index='years',columns='tickers',values='sales')
df = df.reset_index()
df.to_csv('sales-by-years-22.csv', index=False)