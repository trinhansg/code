## Doc bao cao tai chinh
import pandas as pd
###kqdq_amc.csv
df=pd.read_csv('data/kqdq_amc.csv',sep='\t',header=None)
NumRows, NumColumns = df.shape
### Doc ColumnHeaderList
ColumnHeaderList=[]
print(" Vong lap duyet cac cot cua dong 0")
for j in range(1,NumColumns):
    ColumnHeaderList.append(df[j][0])
print("ColumnHeaderList")
print(ColumnHeaderList)
##### #################### doc RowHeaderList
################### doc RowHeaderList
RowHeaderList=[]
print(" Vong lap duyet cac dong cua cot 0")
for i in range(0,NumRows):
    RowHeaderList.append(df[0][i])
print("RowHeaderList")
print(RowHeaderList)
###################################
Row3List=df[3][1:-1]
print("====Row3HeaderList===")
print(Row3List)
print(" In ra tung phan cua dong 3")
for i in range(1,NumColumns):
    print(df[i][3])
###
print(" Vong lap duyet cac dong cua cot 3")
for i in range(0,NumRows):
    print(df[3][i])