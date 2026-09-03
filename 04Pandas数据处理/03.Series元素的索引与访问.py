import pandas as pd

# 位置索引
# ser = pd.Series([11, 22, 33, 44, 55])
# print(ser)
# print(ser[1])

# 标签索引
ser = pd.Series([11, 22, 33, 44, 55], index=['a', 'c', 'c', 'd', 'e'])
# print(ser)
# print(ser['c'])

# # 切片索引
# ## 位置切片(左闭右开)
# print(ser[0:3])
# ## 标签切片(左闭右闭)
# print(ser['b', 'd'])

# loc(标签索引)与iloc(位置索引)
# print(ser.loc['a'])
# print(ser.loc['a':'c'])
#
# print(ser.iloc[2])
# print(ser.iloc[0:2])

"""
at,iat 用于访问元素
head 快速查看Series数据的开头部分内容:
    .head(n=x) n->指定要返回的行数,默认5
tail 查看末尾内容
isin 判断元素是否在指定的一组值中
get 通过标签获取元素
    .get(key, default=None)
    key: 元素的标签
    default: 可选参数, 若key不在标签中,返回该值,默认None
"""
data = [10, 20, 30, 40, 50]
ser = pd.Series(data)
values = [20, 40]
result = ser.isin(values)
print(result)