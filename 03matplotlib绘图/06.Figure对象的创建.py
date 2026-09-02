import matplotlib.pyplot as plt
import numpy as np

# fig = plt.figure(
#     figsize=(5, 5),             # 指定窗口大小
#     facecolor='greenyellow',    # 背景颜色
#     frameon=True,               # 指定是否绘制窗口边框
#     clear=False,                # 是否清除之前的内容
# )
# plt.plot([0, 1], [1, 2])
# plt.figure(num=1)
# plt.plot([0, 1], [2, 3])
# plt.figure(num=1, clear=True)
# plt.plot([0, 1], [3, 4])
# plt.plot(num=1)
# plt.plot([0, 1], [4, 5])
#
# plt.show()

x = np.arange(-10, 10, 0.01)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = 1 / (1 + np.exp(-x))

# 创建一个 2×2 的子图网络
fig, axs = plt.subplots(2, 2, width_ratios=[0.8, 0.2]) # width_ratios -> 设置宽度占比  sharey=True -> 共享y轴

# 第一个子图
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Sine Wave')
axs[0, 0].set_xlabel('X-axis')
axs[0, 0].set_ylabel('Y-axis')

# 第二个
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosine Wave')
axs[0, 1].set_xlabel('X-axis')
axs[0, 1].set_ylabel('Y-axis')

# 第三个
axs[1, 0].plot(x, y3)
axs[1, 0].set_title('Tangent Wave')
axs[1, 0].set_xlabel('X-axis')
axs[1, 0].set_ylabel('Y-axis')

# 第四个
axs[1, 1].plot(x, y4)
axs[1, 1].set_title('Sigmoid Function')
axs[1, 1].set_xlabel('X-axis')
axs[1, 1].set_ylabel('Y-axis')

plt.show()