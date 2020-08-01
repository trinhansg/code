import numpy as np
import matplotlib.pyplot as plt
#Mở file vd.csv để đọc
f = open("data/vd.csv", "r")
#Tạo hai list rỗng
heads=[]
tails=[]
# Đọc từng dòng của file f
for line in f:
    #strip():bo ky tu xuong dong
    # split('): tách chuỗi thành list dựa vào dấu phẩy (,)
    l = line.strip().split(',')
    # Tách ra head và tail
    head,*tail = l
    # Biến đổi các phần tử trong tail thành số nguyên int
    tail = [int(x) for x in tail]
    # Thêm head vào list heads
    heads.append(head)
    # Thêm tail vào list tails
    tails.append(tail)
    # print(newtail)
    # print(l)
    # print(head)
    # print(tail)
print(heads)
print(tails)
# đóng file
f.close()

# nhập tên công ty
name = input("Enter company name: ")
# lấy index của name trong heads
index = heads.index(name)
q = ['Q1','Q2','Q3','Q4']
#vẽ bar chart
#plt.bar(q,tails[index],label=heads[index])
#vẽ line chart
plt.plot(q,tails[index],label=heads[index])
plt.legend()#in chú thích
plt.show()#show biểu đồ