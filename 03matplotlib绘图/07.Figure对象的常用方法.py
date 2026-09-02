import matplotlib.pyplot as plt
from openpyxl.styles.alignment import horizontal_alignments, vertical_aligments

# fig =plt.figure()

# 按照行列创建子图
# ax1 = fig.add_subplot(2, 1, 1)
# ax1.plot([0, 1], [0, 1])
# ax1.set_title('00')
#
# ax2 = fig.add_subplot(2, 1, 2)
# ax2.plot([0, 1], [1, 0])
# ax2.set_title('01')

# 添加一个子图,位于距左边界10%,距下边界10%,宽度为画布50%,高度为画布50%
# ax = fig.add_axes([0.1, 0.1, 0.5, 0.5])
#
# ax.plot([0, 1], [0, 1])

# 超级标题
# ax1 =fig.add_subplot(121)
# ax2 =fig.add_subplot(122)
#
# ax1.plot([0, 1], [0, 1])
# ax2.plot([0, 1], [1, 0])
#
#
# fig.suptitle('Test Suptitle', fontsize=16, color='red')

# 任意位置添加文本
# fig, ax = plt.subplots()
# ax.plot([0, 1, 2], [0, 1, 0])
#
# ax.text(
#     1, 0.5,
#     'Sample Text',
#     fontsize=12,
#     color='red',
#     horizontalalignment='center',   # 水平方向调整对齐方式
#     verticalalignment='center'      # 竖直方向调整对齐方式
# )

# 获取图形中的所有轴
# fig, ax = plt.subplots(2, 2)
# axes = fig.axes
# for ax in axes:
#     print(ax)

# 获取背景颜色
fig = plt.figure(figsize=(8, 6), facecolor='greenyellow')

facecolor = fig.get_facecolor()
print(facecolor)

plt.tight_layout()
plt.show()