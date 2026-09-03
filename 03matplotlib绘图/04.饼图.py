import matplotlib.pyplot as plt

sizes = [25, 35, 20, 20]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

plt.pie(
    sizes,                  # 饼图中每一个扇形的尺寸
    explode=[0, 1, 0, 0],   # 用于指定每个扇形是否突出显示
    labels=labels,          # 标签
    colors=colors,          # 颜色
    autopct='%1.1f%%',      # 显示百分比
    startangle=140,         # 开始角度
    shadow=False,           # 是否添加阴影
    radius=1,               # 半径
    wedgeprops=dict(edgecolor='black', linewidth=2, linestyle='-'),    # 每个扇形的属性
    textprops=dict(color='red', weight='bold'),     # 标签文本的属性
    center=(0, 0),          # 中心位置
    frame=False             # 是否给扇形添加框
)

plt.legend()
plt.show()