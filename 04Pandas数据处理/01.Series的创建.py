import pandas as pd
import numpy as np

# data = 5
# series = pd.Series(data, index=['a', 'b', 'c'], name='test', dtype=np.float64)
# print(series, '\n', type(series))

# data1 = [1, 2, 3, 4, 5]
# ser1 = pd.Series(data1, index=['a', 'b', 1, 2, 3])  # 必须保证 index 中标签数量 >= data 中数据数量
# print(ser1)

# 使用字典创建Series
# data = {'a':1, 'b':2, 'c':3}
# ser = pd.Series(data, index=['x', 'y', 'z'])    # 一般用字典创建Series就不用index设置索引
# print(ser)

# 使用 Ndarray 创建
data = np.array([1, 2 ,3 ,4, 5])
ser = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'], copy=False) # 使用 copy=False 不复制原数据, 会影响到原数据
ser['a'] = 100

print(ser)
print(data)