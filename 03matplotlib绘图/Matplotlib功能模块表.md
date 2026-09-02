# Matplotlib 功能模块表

| 功能模块 | 功能点 | 功能简介 | 功能详情 | 补充说明 |
| --- | --- | --- | --- | --- |
| 线图绘制 | plot 绘制折线图 | 用折线连接坐标点或绘制函数曲线 | plt.plot(x, y, fmt, **kwargs)，fmt 定义线型和颜色；常用参数 label（图例标签）、linewidth（线宽）、color（颜色）、marker（标记样式）、markersize、alpha（透明度） | 曲线点常用 np.arange()、np.linspace() 生成 |
| 线图绘制 | 设置坐标轴比例 | 使 x、y 轴刻度按相同比例显示 | 使用 plt.axis('equal') | 防止图形在窗口中被拉伸变形 |
| 散点图 | scatter 绘制散点图 | 绘制数据点分布，颜色可随数值映射 | plt.scatter(x, y, s, c, marker, cmap, vmin, vmax, alpha, linewidths, edgecolors) | c 传入 y 值数组并结合 cmap 时，点的颜色随数值渐变 |
| 散点图 | 添加颜色条 | 显示颜色映射对应的数值标尺 | 使用 plt.colorbar() 添加颜色条 | 需配合 cmap 使用效果直观 |
| 条形图 | bar 绘制条形图 | 用条形高度表示类别数值的大小 | plt.bar(labels, values, width, color, edgecolor, linewidth, linestyle, hatch, align, label) | 支持 hatch 填充图案、alpha 透明度 |
| 饼图 | pie 绘制饼图 | 用扇形展示各部分占总体的比例 | plt.pie(sizes, explode, labels, colors, autopct, startangle, shadow, radius, wedgeprops, textprops) | autopct='%1.1f%%' 显示百分比；explode 指定扇形是否突出分离 |
| 标题与标签 | 轴标签与图题 | 为图形添加标题和坐标轴说明 | 使用 plt.title()、plt.xlabel()、plt.ylabel() | 图例使用 plt.legend()，内容取自绘图的 label 参数 |
| 子图布局 | subplot 分区绘制 | 在同一窗口中按行列划分位置绘制多个子图 | plt.subplot(rows, cols, index) 后按普通方式绘图 | 子图绘制完成后用 plt.tight_layout() 自动调整间距 |
| Figure 创建 | figure 创建图形对象 | 手动创建独立的 Figure 窗口 | plt.figure(figsize=(宽, 高), facecolor=背景色, frameon=边框, clear=是否清空) | num 参数可切换/定位窗口，配合 clear=True 清空重绘 |
| Figure 创建 | subplots 创建子图网络 | 一次创建 Figure 和多个 Axes 子图对象 | fig, axs = plt.subplots(2, 2, width_ratios=[0.8, 0.2], sharey=True) | width_ratios 设置各列宽度占比，sharey 共享 y 轴；axs[i, j] 定位子图 |
| Figure 创建 | 用 Axes 对象绘图 | 通过返回的 Axes 在指定子图内绘制并修饰 | ax.plot()、ax.set_title()、ax.set_xlabel()、ax.set_ylabel() | 与 plt.title() 等作用等价，但只作用于对应子图 |
| Figure 常用方法 | 手动添加子图与坐标轴 | 向已有 Figure 添加子图或任意位置的坐标轴 | fig.add_subplot(2, 1, 1)、fig.add_axes([0.1, 0.1, 0.5, 0.5]) | add_axes 参数为 [左, 下, 宽, 高] 的相对坐标 |
| Figure 常用方法 | 文本与超级标题 | 在任意位置添加文本，或为整个 Figure 添加总标题 | ax.text(x, y, 文本, fontsize, color, horizontalalignment, verticalalignment)、fig.suptitle() | suptitle 针对整个图形，title 只针对单个子图 |
| Figure 常用方法 | 获取图形信息 | 获取 Figure 中的所有 Axes 或背景颜色 | 使用 fig.axes、fig.get_facecolor() | 便于批量处理所有子图或调试样式 |
