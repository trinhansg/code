# create dataframes from dicts
import pandas as pd
# create a dict
data = {
	'apples': [3, 2, 0, 1],
	'oranges': [0, 3, 7, 2]
}
# create a dataframe
# df = pd.DataFrame(data)
# df = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
df = pd.DataFrame(data, index=range(100,104))
# print the dataframe
print(df)