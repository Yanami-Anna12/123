import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 3 * np.pi, 0.1)
y = np.sin(x)

# plt.plot(
#     x, y,    # "-" -> 实线型
#     label='Sine Wave',  # 图例标签
#     linewidth=2,        # 线宽
#     color='blue',       # 线的颜色
#     # marker='.',         # 标记样式
#     markersize=5,       # 标记大小
#     markeredgecolor='black',  # 标记边缘的颜色
#     markeredgewidth=1,  # 标记边缘的宽度
#     markerfacecolor='none',   # 标记内部颜色
#     alpha=1,          # 透明度
# )
#
# # 显示轴标签
# plt.xlabel('x')
# plt.ylabel('y')
# # 显示图题
# plt.title('Sine Wave')
#
# plt.show()


y_sin = np.sin(x)
y_cos = np.cos(x)

# 在第一个位置创建子图
plt.subplot(2, 1, 1) # 2行1列, 第一个子图
plt.plot(x, y_sin)
plt.title('Sine Wave')
plt.xlabel('x')
plt.ylabel('y_sin')
plt.axis('equal')

# 在第二个位置创建子图
plt.subplot(2, 1, 2) # 2行1列, 第二个子图
plt.plot(x, y_cos)
plt.title('Cosine Wave')
plt.xlabel('x')
plt.ylabel('y_cos')
plt.axis('equal')

# 调用 tight_layout 来自动调整子图参数
plt.tight_layout()

plt.show()