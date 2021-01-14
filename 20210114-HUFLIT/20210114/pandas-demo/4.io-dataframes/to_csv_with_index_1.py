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
# save the dataframe to a csv file with the index
df.to_csv('output1.csv')
# df.to_csv('d:/@pyspark/output1.csv')
# df.to_csv(r'd:\@pyspark\output1.csv')