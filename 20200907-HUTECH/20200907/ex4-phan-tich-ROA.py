# Chuong trinh tinh ROA
lairong=float(input("Lai rong: "))
Taisan=float(input("Tong Tai san: "))
TysoROA=lairong/Taisan
if TysoROA>0.1:
    print("Hieu qua cao")
elif TysoROA>=0.05:
    print("Hieu qua Trung binh")
else:
    print("Hieu qua thap")