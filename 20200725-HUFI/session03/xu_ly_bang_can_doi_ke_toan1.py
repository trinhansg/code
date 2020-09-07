import numpy as np
#Khai bao bang can doi ke toan bang bang 2D
arr= np.array([
    [185709,193420,186423,135724],
    [12793,13460,12870,19450],
    [13240,12370,14750,16870],
    [32535,36466,31270,41286]
])
#Khai bao 2 list:
column_header_list=["Q4-2019","Q3-2019","Q2-2019","Q1-2019"]
row_header_list=["Tai san ngan han",
                 "Tien va cac khoan tuong duong",
                 "Cac khoan dau tu tai chinh",
                 "Cac khoan phai thu ngan han"]
row = int(input("Nhap dong: "))
col = int(input("Nhap cot: "))
print(column_header_list[col])
print(row_header_list[row])
print("Gia tri: ",arr[row][col])
