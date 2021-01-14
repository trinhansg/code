# create dataframes from dicts
import pandas as pd
# create a dict
data = {
	'apples': [3, 2, 0, 1],
	'oranges': [0, 3, 7, 2]
}
# create a dataframe
df = pd.DataFrame(data)
print(df)
# save the dataframe to a csv file without the index
df.to_csv('output3.csv', index=False)