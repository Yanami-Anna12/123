""""""
"""
count 计算非空值的数量
sum 计算和
mean 计算平均值
mdeian 中位数
min max 
var 方差
std 标准差
quantile 分位数
    计算方法:
        假设Series长度为n, 计算第q个分位数的位置下标:
                        index = q × (n - 1)
        if index is int: 直接去该位置的值
        else:
            记 index = i(int) + f(float)
            则分位数 Q=Xi + f*(X(i+1) - Xi)
cummax 计算元素累计最大值
cummin
cumsum 累积和
cumprod 累计积
"""