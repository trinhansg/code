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
            if row==[]:
                break
            if i==1:
                DongTieuDe=row
                i=i+1
            else:
                TempArray=[]
                for j in range(len(row)):
                    TempArray.append(row[j])
                DongChiTiet.append(TempArray)
    return DongTieuDe,DongChiTiet


DongTieuDe1,DongChiTiet1=readfilecsv('data/kqdq_ads.csv')
DongTieuDe2,DongChiTiet2=readfilecsv('data/kqdq_aav.csv')
print("**** Dong tieu de 1-data/kqdq_ads.csv ")
print(DongTieuDe1)
print("Dong tieu de 2data/kqdq_aav.csv")
print(DongTieuDe2)

Cube=[]
Cube.append(DongChiTiet1)
Cube.append(DongChiTiet2)
print("Phan tu cua mang 3 chieu")
print("Cong ty Dong tieu de 1-data/kqdq_ads.csv")
print(Cube[0][0])
print(Cube[0][0][0])

print("Cong ty Dong tieu de 2-data/kqdq_aav.csv")
print(Cube[1][0])
print(Cube[1][0][0])
print(Cube[1][0][1])
