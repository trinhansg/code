import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
# tạo dataframe df từ file banks.csv
df = read_csv(r'banks.csv',comment='#')
# in 20 dòng đầu tiên của dataframe df
print(df.head(20))
# in kiểu dữ liệu của các cột của dataframe df
print(df.dtypes)
# in tên cột của dataframe df
print(df.columns)
# thêm cột ROA và ROE vào dataframe df
df['ROA'] = df['loi_nhuan_sau_thue']/df['tong_tai_san']
df['ROE'] = df['loi_nhuan_sau_thue']/df['vcsh']
# tạo dataframe hose bằng cách lọc dataframe df với điều kiện
# 'san' == 'HoSE'
hose = df[df.san=='HoSE']
# đếm các giá trị khác rỗng của cột 'ma_ck' của dataframe df
print(df['ma_ck'].count())
# in các cột ['ma_ck', 'ten_cong_ty','loi_nhuan_sau_thue','tong_tai_san','vcsh','ROA','ROE']
# của datafrane df
print(df[['ma_ck', 'ten_cong_ty','loi_nhuan_sau_thue','tong_tai_san','vcsh','ROA','ROE']])



