f = open("data/vd.csv", "r", encoding='UTF8')
# Đọc từng dòng của file f
for line in f:
    #strip():bo ky tu xuong dong
    print(line.strip())
f.close()