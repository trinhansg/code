import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
from mylib.viz import autolabel

# tạo dataframe df từ file banks.csv
df = read_csv(r'banks.csv',comment='#')
# tạo dataframe df mới chỉ chứa ['VCB','VPB']
df = df[df.ma_ck.isin(['VCB','VPB'])]
# thêm cột ROA và ROE vào dataframe df
df['ROA'] = df['loi_nhuan_sau_thue']/df['tong_tai_san']
df['ROE'] = df['loi_nhuan_sau_thue']/df['vcsh']
print('Dataframe truoc khi pivot:')
print(df)
df = df.pivot(index='nam', # chọn cột 'nam' làm index
              columns='ma_ck', # chọn cột 'ma_ck' xoay ngang để tạo các cột mới
              values='ROE' # chọn cột 'ROE' làm values
              ).reset_index() # tạo lại index, cột 'nam' trở thành cột bình thường của dataframe
print('Dataframe sau khi pivot:')
print(df)
# vẽ biểu đồ ROE của ['VCB','VPB']
ax = df.plot.bar(x='nam', y=['VCB','VPB'],
                    color=[np.random.rand(3),np.random.rand(3)], # màu ngẫu nhiên
                    rot=30, # xoay nhãn trục x một góc 30 độ
                    figsize=(12,6)) # qui định kích thước biểu đồ 10 inch x 6 inch
# gắn nhãn dữ liệu với định dạng phần trăm với 2 số lẻ
autolabel(ax, ax.patches, num=2, percent=True)
plt.title("ROE Của VCB & VPB Qua Các Năm")
plt.xlabel("Năm")
plt.ylabel("ROE")
plt.tight_layout()
plt.show()