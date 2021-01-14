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
# print head(n) rows
print(df.head(3))
# print tail(n) rows
print(df.tail(3))
# print top(3) rows
print(df[:3])
# print from row 1 to row 2
print(df[1:3])
# print the row with index 1
print(df.loc[1])
print(df.iloc[1])
