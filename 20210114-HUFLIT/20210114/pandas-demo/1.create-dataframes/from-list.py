# create dataframes from lists
import pandas as pd
# create a list
data = [['Alex',10],['Bob',12],['Clarke',13]]
# create a dataframe from the list
df = pd.DataFrame(data,columns=['Name','Age'])
# print the dataframe
print(df)