#### Tinh cosineSimilarity
## Cho 3 diem thuoc R^4
import math
A=[1,1,1,1]
B=[1,1,1,1]
C=[5,5.1,5,5]
### TInh he so cosSim A,B
### TInh he so cosSim A,C
def CosSim(X,Y):
    Tuso=0.0000
    for i in range(len(X)):
        Tuso+= X[i]*Y[i]
     ## Norm
    MauSo1=0.0000
    for i in range(len(X)):
        MauSo1+= X[i]*X[i]

    a=math.sqrt(MauSo1)
    MauSo2 = 0.0000
    for i in range(len(Y)):
        MauSo2 += Y[i] * Y[i]
    b = math.sqrt(MauSo2)
    Sim=Tuso/(a*b)
    return Sim

def EuclideanDistance(X,Y):
    Dist = 0.0000
    for i in range(len(Y)):
        Dist += (X[i] -Y[i])**2
    Dist = math.sqrt(Dist)
    return Dist

print("Cosine Similarity of A,B={:5.2f}".format(CosSim(A,B)))
print("CosSine Similarity of A,C={:5.2f}".format(CosSim(A,C)))

print("EuclideanDistance of A,B={:5.2f}".format(EuclideanDistance(A,B)))
print("EuclideanDIstance of A,C={:5.2f}".format(EuclideanDistance(A,C)))
ToaDo=[[0.9,2.9],[1.1,2.9],[1.0,2.5],[3.7,1.0],[3.9,0.9]]
for i in range(len(ToaDo)):
    print("Diem X ",i,"=",ToaDo[i][0])
    print("Diem Y ", i, "=",ToaDo[i][1])

for i in range(len(ToaDo)):
    for j in range(len(ToaDo)):
        X = ToaDo[i]
        Y = ToaDo[j]
        a=EuclideanDistance(X, Y)
        print("Khoang cach tu diem {:3d} den {:3d} la  {:5.2f}".format(i,j, a))

