####H:\BaiGiang2020\2020_AI_DataAnalyticsAccouting\PythonPhanTichDuLieu\DocNhieuFileToChucCube.py
import csv
def readfilecsv(filename):
    print("Ten file="+filename)
    with open(filename,encoding="utf8") as csvfile:
        readCSV = csv.reader(csvfile, delimiter='\t')
        i=1
        DongTieuDe=[]
        DongChiTiet=[]
        for row in readCSV:
            print(row)
            # if row==[]:
            #     pass
            #     # break
            if i==1:
                DongTieuDe=row
                i=i+1
            else:
                TempArray=[]
                for j in range(len(row)):
                    TempArray.append(row[j])
                DongChiTiet.append(TempArray)
    return DongTieuDe,DongChiTiet


companies = ['ads','aav','aam']

DongTieuDe1,DongChiTiet1=readfilecsv('data/kqdq_ads.csv')
DongTieuDe2,DongChiTiet2=readfilecsv('data/kqdq_aav.csv')
DongTieuDe3,DongChiTiet3=readfilecsv('data/kqdq_aam.csv')
print("**** Dong tieu de 1-data/kqdq_ads.csv ")
print(DongTieuDe1)
print("Dong tieu de 2data/kqdq_aav.csv")
print(DongTieuDe2)

Cube=[]
Cube.append(DongChiTiet1)
Cube.append(DongChiTiet2)
Cube.append(DongChiTiet3)
print("Phan tu cua mang 3 chieu")
print("Cong ty Dong tieu de 1-data/kqdq_ads.csv")
print(Cube[0][0])
print(Cube[0][0][0])#Cong ty, dong, cot
print(Cube[0][0][1])
print(Cube[0][0][2])

print("Cong ty Dong tieu de 2-data/kqdq_aav.csv")
print(Cube[1][0])
print(Cube[1][0][0])
print(Cube[1][0][1])
print(Cube[1][0][2])

print("Cong ty Dong tieu de 3-data/kqdq_aam.csv")
print(Cube[2][0])
print(Cube[2][0][0])
print(Cube[2][0][1])
print(Cube[2][0][2])
# ROA=loinhuan/Tongtaisan
print('Loi nhuan: ',Cube[2][48])
print('Tong tai san: ',Cube[2][16])
print(f"ROA: {float(Cube[2][48][1])/float(Cube[2][16][1]):,.6f}")
roa = float(Cube[2][48][1])/float(Cube[2][16][1])
# ROS=loinhuan/Doanhthuthuan
print('Doanh thu thuan: ',Cube[2][33])
print(f"ROS: {float(Cube[2][48][1])/float(Cube[2][33][1]):,.6f}")
ros = float(Cube[2][48][1])/float(Cube[2][33][1])
print(f"AAM,{roa},{ros}")



f = open("data/data.csv", "w", encoding='utf8')
for i in range(len(companies)):
    roa = float(Cube[i][48][1]) / float(Cube[i][16][1])
    ros = float(Cube[i][48][1]) / float(Cube[i][33][1])
    print(f"{companies[i]},{roa},{ros}\n")
    f.write(f"{companies[i]},{roa},{ros}\n")
f.close()

