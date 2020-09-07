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
## Tim phan tu lon nhat
max=arr[0][0] # gia dinh phan tu max la phan tu dau tien
jmax=0
for j in range(1,4):
    ## xet phan tu arr[0][j]
    if arr[0][j] >max:
        max=arr[0][j]
        jmax=j
print("Quy co tai san ngan han lon nhat la ",column_header_list[jmax])
print("gia tri max=",arr[0][jmax])
### tim phan tu nho nhat
while (1):
    chiso=int(input("Cho chi so dong (so am de ket thuc):"))
    if chiso < 0:
        break
    min=arr[chiso][0] # gia dinh phan tu max la phan tu dau tien
    jmin=0
    for j in range(1,4):
        ## xet phan tu arr[0][j]
        if arr[chiso][j] < min:
            min=arr[chiso][j]
            jmin=j
    print(row_header_list[chiso],column_header_list[jmin])
    print("gia tri min=",arr[chiso][jmin])
