# create dataframes from dicts
import pandas as pd
# create a dict
data = {
	'apples': [3, 2, 0, 1],
	'oranges': [0, 3, 7, 2]
}
# create a dataframe
df = pd.DataFrame(data)
# print the dataframe
print(df)
# select one column
print(df['apples'])
# select multi-columns
print(df[['apples','oranges']])
# select data by columns and rows
print(df[['apples','oranges']][:3])
