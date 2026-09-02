import matplotlib.pyplot as plt

labels = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 33]

plt.bar(
    labels, values,
    width=0.3,      # 条形的宽度
    color='b',      # 条形的填充颜色
    edgecolor='r',  # 条形边缘的颜色
    linewidth=2,     # 条形边缘的线宽
    linestyle='-',  # 条形边缘的线型
    alpha=0.7,      # 透明度
    hatch='-',      # 填充图案
    align='center', # 对齐方式
    label='test'    # 创造图例时使用的标签
)

plt.legend()
plt.show()