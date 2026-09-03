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
| 子图布局 | GridSpec 网格布局 | 先声明行数、列数划分网格，再把子图放到指定网格位置 | gs = GridSpec(nrows, ncols)；fig.add_subplot(gs[i, j]) | 需配合 figure() 使用，布局比 subplot 更灵活 |
| 子图布局 | GridSpec 跨格子图 | 让一个子图横跨多行或多列，实现大小不一的不规则排版 | 用切片定位，如 fig.add_subplot(gs[1, 1:]) 表示占据第 2 行第 2、3 列 | 类似表格的"合并单元格"，可让不同子图宽度/高度不同 |
| Figure 创建 | figure 创建图形对象 | 手动创建独立的 Figure 窗口 | plt.figure(figsize=(宽, 高), facecolor=背景色, frameon=边框, clear=是否清空) | num 参数可切换/定位窗口，配合 clear=True 清空重绘 |
| Figure 创建 | subplots 创建子图网络 | 一次创建 Figure 和多个 Axes 子图对象 | fig, axs = plt.subplots(2, 2, width_ratios=[0.8, 0.2], sharey=True) | width_ratios 设置各列宽度占比，sharey 共享 y 轴；axs[i, j] 定位子图 |
| Figure 创建 | 用 Axes 对象绘图 | 通过返回的 Axes 在指定子图内绘制并修饰 | ax.plot()、ax.set_title()、ax.set_xlabel()、ax.set_ylabel() | 与 plt.title() 等作用等价，但只作用于对应子图 |
| Figure 常用方法 | 手动添加子图与坐标轴 | 向已有 Figure 添加子图或任意位置的坐标轴 | fig.add_subplot(2, 1, 1)、fig.add_axes([0.1, 0.1, 0.5, 0.5]) | add_axes 参数为 [左, 下, 宽, 高] 的相对坐标 |
| Figure 常用方法 | 文本与超级标题 | 在任意位置添加文本，或为整个 Figure 添加总标题 | ax.text(x, y, 文本, fontsize, color, horizontalalignment, verticalalignment)、fig.suptitle() | suptitle 针对整个图形，title 只针对单个子图 |
| Figure 常用方法 | 获取图形信息 | 获取 Figure 中的所有 Axes 或背景颜色 | 使用 fig.axes、fig.get_facecolor() | 便于批量处理所有子图或调试样式 |
| Figure 常用方法 | 设置尺寸与分辨率 | 获取/修改图形大小与分辨率 | fig.get_dpi()/set_dpi()、fig.get_size_inches()/set_size_inches(8, 6) | set_size_inches 创建图形后仍可改尺寸，常与 set_dpi 配合使用 |
| Figure 常用方法 | 获取当前图形与坐标轴 | 获取当前活动的 Figure 或 Axes 对象以便继续修饰 | plt.gcf() 返回当前图形（无则新建）；plt.gca()（get current axis）返回当前坐标轴；ax.get_label() 获取坐标轴标签 | 取回对象后可继续调用 set_title、set_xlabel 等方法 |
| Figure 常用方法 | 手动调整子图布局 | 自动排满画布不重叠，或手动调节子图边距与间距 | plt.tight_layout() 自动调整；fig.subplots_adjust(left, bottom, right, top, wspace, hspace) 手动调整 | wspace/hspace 为子图间水平/垂直间距，范围 0~1 |
| Figure 常用方法 | 清除与关闭 | 清除单个轴或整个图形的元素，并关闭窗口 | ax.clear() 清除该轴上的图形元素；fig.clear()/plt.clf() 清除所有子图与元素；plt.close() 关闭一个或多个窗口 | clf 归属于 pyplot 库，作用与 Figure.clear 类似 |
| 图形输出 | 显示图像 | 将二维数组以图像形式显示 | plt.imshow(x, cmap=, norm=, aspect=, interpolation=, alpha=, vmin=, vmax=, origin=) | cmap 指定颜色映射；vmin/vmax 设置映射范围；可配合 colorbar 观察数值 |
| 图形输出 | 保存图形 | 将当前图形保存为图片文件 | plt.savefig('plot.png', dpi=300, bbox_inches='tight', facecolor='greenyellow') | bbox_inches='tight' 自动裁剪四周空白 |
| 图形输出 | 暂停与动态刷新 | 绘图后暂停脚本执行并刷新窗口，实现逐帧动画 | plt.show(block=False) 后循环内更新数据并调用 plt.pause(0.01) | pause(interval) 暂停 interval 秒并刷新；动画结束后用 plt.close() 收尾 |
