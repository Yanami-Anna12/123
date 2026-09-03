import matplotlib.pyplot as plt
import numpy as np
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
# fig = plt.figure(figsize=(8, 6), facecolor='greenyellow')
#
# facecolor = fig.get_facecolor()
# print(facecolor)

# get_dpi 用于获取图形分辨率

# get_gca -> get current axis 的缩写, 用于获取当前图形的坐标轴对象
# plt.figure()
# plt.plot([1, 2, 3], [1, 2, 3])
#
# # 获取当前坐标轴
# ax = plt.gca()
#
# ax.set_title('Sample Plot')
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')

"""
get_label 用于获取坐标轴的标签
get_size_inches 获取英尺
set_size_inches 用于设置图形大小, 可以在创建图形后改变其尺寸
set_dpi 设置分辨率,通常与 set_size_inches 配合使用
tight_layout 用于自动调整子图参数, 填充整个图像并确保不重叠
subplots_adjust 允许手动调整子图空间,使用例:
    subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=None)
    wspace: 子图之间的水平间距,范围0~1
    hspace: 子图之间的垂直间距,范围0~1
clear Axes对象的clear清除该轴上的所有图形元素;Figure的clear清除所有的子图与元素
clf 与Figure的clear类似,但归属于pyplot库
imshow 用来显示二维数组:
    imshow(x, cmap= , norm= , aspect= , interpolation= , alpha= , vmin= , vmax= , origin= , **kawrgs)
    x: 图像数据, 一般是二维数组,也可以是一堆数组,int or float
    cmap: 颜色映射, 用于指定图像中数值颜色的映射
    norm: 用于标准化数据值的归一化对象
    aspect: 控制图像的纵横比
    interpolation: 指定图像缩放时的插值方法
    alpha: 透明度
    vmin, vmax: 指定颜色映射范围
    origin: 指定图像原点,
    **kwargs: 其他关键字参数
close 用于关闭一个or多个窗口
"""
# gcf 用于返回当前活动的图形对象,若无则创建一个新的
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3], [1, 2, 3])
# current_fig = plt.gcf()
# current_fig.set_size_inches(8, 6)
# current_fig.suptitle("Example Plot")

# savefig 用于将当前图形保存至文件中
# x = [0, 1, 2, 3, 4]
# y=[0, 1, 4, 9, 16]
# plt.plot(x, y)
# plt.savefig('plot.png', dpi=300, bbox_inches='tight', facecolor='greenyellow')

# pause 用于在动画or交互过程中暂停一段时间
# 调用 plt.pause(interval) 时, python脚本会暂停执行指定的时间
# 若在绘图之前调用了plt.pause, 允许动态更新的图形显示
fig, ax = plt.subplots()
t = np.arange(0, 10, 0.01)
s = np.sin(t)
ax.plot(t, s)
plt.show(block=False)
for phase in np.arange(0, 2*np.pi, 0.05):
    ax.plot(t + phase, np.sin(t+phase))
    plt.pause(0.01)
plt.close()

# plt.tight_layout()
plt.show()