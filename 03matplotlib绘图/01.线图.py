import matplotlib.pyplot as plt
import numpy as np

# # plot([x1, x2], [y1 ,y2], fmt, **kwargs) 从(x1, y1)到(x2, y2)的直线, fmt 用于定义图形的颜色和样式
# plt.plot([0, 3], [0, 2])
# plt.show()

# 计算曲线上点的x,y坐标
# x = np.arange(0, 3 * np.pi, 0.1)
# x = np.linspace(0, 10 * np.pi, 500)
# y = np.sin(x)
x = np.linspace(0, 10, 10)
y = 2 * x + 1

plt.plot(
    x, y, '-',    # "-" -> 实线型
    label='Sine Wave',  # 图例标签
    linewidth=2,        # 线宽
    color='blue',       # 线的颜色
    # marker='.',         # 标记样式
    markersize=5,       # 标记大小
    markeredgecolor='black',  # 标记边缘的颜色
    markeredgewidth=1,  # 标记边缘的宽度
    markerfacecolor='none',   # 标记内部颜色
    alpha=1,          # 透明度
)

# 设置x,y轴相同比例
plt.axis('equal')

plt.legend()
plt.show()