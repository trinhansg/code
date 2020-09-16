import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
from mylib.viz import autolabel

# tạo dataframe df từ file banks.csv
df = read_csv(r'banks.csv',comment='#')
# tạo dataframe df mới bằng cách lọc dataframe df cũ với điều kiện
# 'san' == 'HoSE'
# df mới chỉ chứa thông tin ngân hàng của sàn HoSE
df = df[df.san=='HoSE']
# thêm cột ROA và ROE vào dataframe df
df['ROA'] = df['loi_nhuan_sau_thue']/df['tong_tai_san']
df['ROE'] = df['loi_nhuan_sau_thue']/df['vcsh']
# tạo dfVCB mới chỉ chứa thông tin VCB
dfVCB = df[df.ma_ck.isin(['VCB'])]
# đếm số năm
so_nam = dfVCB['nam'].count()
# vẽ biểu đồ ROA của VCB
ax = dfVCB.plot.bar(x='nam', y='ROA',
                    color=np.random.rand(so_nam,3), # màu ngẫu nhiên
                    rot=30, # xoay nhãn trục x một góc 30 độ
                    figsize=(10,6)) # qui định kích thước biểu đồ 10 inch x 6 inch
# gắn nhãn dữ liệu với định dạng phần trăm với 2 số lẻ
autolabel(ax, ax.patches, num=2, percent=True)
plt.title("ROA Của VCB Qua Các Năm")
plt.xlabel("Năm")
plt.ylabel("ROA")
plt.tight_layout()
# vẽ biểu đồ ROE của VCB
ax = dfVCB.plot.bar(x='nam', y='ROE', color=np.random.rand(so_nam,3), rot=30, figsize=(10,6))
autolabel(ax, ax.patches, num=2, percent=True)
plt.title("ROE Của VCB Qua Các Năm")
plt.xlabel("Năm")
plt.ylabel("ROE")
plt.tight_layout()
# cho hiện các biểu đồ
plt.show()
