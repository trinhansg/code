from sklearn.linear_model import LinearRegression
# Tập học
X = [[6], [8], [10], [14], [18]]
y = [[7], [9], [13], [17.5], [18]]
# Tạo model hồi quy tuyến tính
model = LinearRegression()
model.fit(X, y)
print ('A 12" pizza should cost: $%.2f' % model.predict([[12]]))
# Kết quả #### A 12" pizza should cost: $13.68
