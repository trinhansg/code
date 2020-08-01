import numpy as np

f = open("data/vd.csv", "r")
# Đọc từng dòng của file f
for line in f:
    #strip():bo ky tu xuong dong
    #split('): tách chuỗi thành list dựa vào dấu phẩy (,)
    l = line.strip().split(',')
    # Tách ra head và tail
    head,*tail = l
    print(l)
    print(head)
    print(tail)
f.close()