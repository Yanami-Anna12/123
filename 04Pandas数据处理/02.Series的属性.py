import pandas as pd

# ser = pd.Series([1, 2, 3], index=[1, 2, 3])
# print(ser.index)

# 重新给Series对象的索引赋值
# ser.index = ['a', 'b', 'c']
# print(ser)
# print(ser.values)

"""
values 用于返回Series中的数据, 数据以Ndarray数组的形式存在
name 用于返回Series的名称
dtype/dtypes 返回Series对象的数据类型
shape 描述Series的形状
size 返回Series元素数量
empty 判断Series是否为空
hasnans 判断是否包含NAN
is_unique 判断是否唯一
nbytes 返回所有数据占用的总字节数
axes 返回对象行轴标签的列表
ndim 返回维度
array 返回Series的底层数组,包括数组的元素,长度以及数组元素的数据类型
attrs 返回自定义属性, 可用来储存额外的说明性数据
is_monotonic_decreasing 判断是否降序排列
is_monotonic_increasing
"""

ser = pd.Series([1, 2, 3, 4, 5])
print(ser.attrs)

ser.attrs = {'source': 'file1', 'time':'11:45:14'}

print(ser)
print("额外属性:", ser.attrs)