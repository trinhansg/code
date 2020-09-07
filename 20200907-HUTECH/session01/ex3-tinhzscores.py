A = input("Nhap A: ")
B = input("Nhap B: ")
C = input("Nhap C: ")
D = input("Nhap D: ")
E = input("Nhap E: ")
# Tinh Z-Score Altman
Z = 1.2*float(A) + 1.4*float(B) + 3.3*float(C) \
    + 0.6*float(D) + 1.0*float(E)
print("Z-Score: ", Z)
if Z >= 3.0:
    print("An toan ")
else:
    print(" Khong an toan ")