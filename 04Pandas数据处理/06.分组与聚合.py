""""""
"""
groupby 用于将series数据分组
agg 用于数据聚合
"""
import pandas as pd
s = pd.Series([1, 2, 3, 4, 5])

result = s.agg('mean')
print(result)

result = s.agg(['max', 'min'])
print(result)

result = s.agg({"Maximun":'max', "Minmun":'min'})
print(result)

def custom_agg(x, power):
    return (x ** power).sum()

result = s.agg(custom_agg, power=2)
print(result)