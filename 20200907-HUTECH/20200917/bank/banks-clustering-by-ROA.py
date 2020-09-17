import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas import read_csv
from mylib.viz import autolabel

# tạo dataframe df từ file banks.csv
df = read_csv(r'banks.csv',comment='#')
# thêm cột ROA và ROE vào dataframe df
df['ROA'] = df['loi_nhuan_sau_thue']/df['tong_tai_san']
df['ROE'] = df['loi_nhuan_sau_thue']/df['vcsh']
# Tạo pivot table
df = df.pivot(index='ma_ck',
              columns='nam',
              values='ROA'
              ).reset_index()
# Lưu df vào file
df.to_csv('bank-clustering-by-ROA.csv', index=False)