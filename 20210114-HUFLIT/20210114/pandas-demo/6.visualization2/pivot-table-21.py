from pandas import read_csv

df = read_csv('sales-by-years-2.csv')
df = df.pivot(index='tickers', columns='years', values='sales')
df = df.reset_index()
df.to_csv('sales-by-years-21.csv', index=False)