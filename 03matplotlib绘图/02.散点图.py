import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

colors = y

plt.scatter(
    x, y,
    s=10,           # 散点的大小
    c=colors,       # 散点的颜色, 这里使用y值映射颜色
    marker='.',     # 散点的标记样式
    cmap='viridis', # 颜色映射
    norm=None,      # 默认的标准化
    vmin=-3,        # 颜色映射的最小值
    vmax=3,         # 最大值
    alpha=1,      # 透明度
    linewidths=0.5,  # 散点边缘的线宽
    edgecolors='w'
)

# 添加颜色条
plt.colorbar()

plt.legend()
plt.show()