""""""
"""
unique 返回Series中唯一的值
nunique 统计唯一值的数量
value_counts 统计每一个值出现的次数,返回值 次数的Series
describe 生成描述性统计信息
copy 创建Series对象的副本(深浅拷贝)
reset_index 重置索引,将原索引转换为一个列, 并将一个新的默认整数索引赋值给Series
info 显示概要信息
apply 对Series中每个元素应用一个函数,并返回一个结果
map 对每个元素应用一个映射, 允许将一个函数应用到Series每一个元素, 或者将一个自定or Series映射到Series的值上

"""
import pandas as pd
s = pd.Series([1, 2, 3, 4, 5])
s1 = pd.Series([50, 60, 70, 80, 90], index=['a', 'b', 'c', 'd', 77])
grades = pd.Series([80, 92, 77, 59, 100], index=[0, 1, 2, 3, 4])
# res = ser.apply(lambda s:s ** 3)
# def double(x):
#     return x * 2
# s_double = s.map(double)
# print(s_double)
print(s1)
print(grades)
res = grades.map(s1)
print(res)