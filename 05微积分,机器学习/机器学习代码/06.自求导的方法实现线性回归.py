import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs

# 1.散点输入
data = [[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4, -15.7], [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6], [0.4, 34.0], [0.8, 62.3]]

data = np.array(data)
x_data = data[:, 0]
y_data = data[:, 1]

# 2.初始化数据
w = 0
b = 0
learning_rate = 0.01

# 3.绘图
fig = plt.figure(figsize=(12, 6))
# 创建一个包含2行2列的布局对象
gs = gs.GridSpec(2, 2)
# 左上格子
ax2 = fig.add_subplot(gs[0, 0])
ax2.set_xlabel("X")
ax2.set_ylabel("Y")
# 左下格子
ax3 = fig.add_subplot(gs[1, 0])
ax3.set_xlabel("w")
ax3.set_ylabel("b")
# 右侧格子
# projection 指定这个子图是3D的投影图像对象
ax1 = fig.add_subplot(gs[:, 1], projection='3d')
# 构建3D网格
w_values = np.linspace(-20, 80, 100)
b_values = np.linspace(-20, 80, 100)
W, B = np.meshgrid(w_values, b_values)
loss_values = np.zeros_like(W)
ax1.plot_surface(W, B, loss_values)

# 损失函数
def loss_function(X, Y, w, b):
    _y_hat = X * w + b
    loss = np.mean((_y_hat - Y) ** 2)
    return loss

# 计算每个网格点的损失值
for i, w in enumerate(w_values):
    for j, b in enumerate(b_values):
        loss_values[j, i] = loss_function(x_data, y_data, w, b)

# 绘制3D图
ax1.plot_surface(W, B, loss_values, alpha=0.7, cmap='viridis')

ax1.set_xlabel('w')
ax1.set_ylabel('b')
ax1.set_zlabel('loss')


# 4.开始迭代
num_iterations = 500
path = []
for n in range(1, num_iterations+1):
    ax2.cla()
    path.append((w, b))
    # 5.反向传播
    y_hat = w * x_data + b
    gradient_w = np.mean(2 * (y_hat - y_data) * x_data)
    gradient_b = np.mean(2 * (y_hat - y_data))
    # 更新参数
    w -= learning_rate * gradient_w
    b -= learning_rate * gradient_b
    # 6.显示频率设置
    if n % 10 == 0 or n == 1:
        # 7.梯度下降的显示
        x_min = x_data.min()
        x_max = x_data.max()
        y_min = w * x_min + b
        y_max = w * x_max + b
        ax2.scatter(x_data, y_data)
        ax2.plot([x_min, x_max], [y_min, y_max], c='r')

        ax3.contourf(W, B, loss_values, levels=20)
        ax3.scatter(w, b, c='r')
        ax1.scatter(w, b, loss_function(x_data, y_data, w, b), c='r')

        if len(path) > 0:
            path_w, path_b =zip(*path)
            ax3.plot(path_w, path_b, c='r')
            path_w = np.array(path_w)
            path_b = np.array(path_b)
            z_loss = np.array([loss_function(x_data, y_data, w, b) for w, b in zip(path_w, path_b)])
            ax1.plot(path_w, path_b, z_loss, c='r')
            # ax1.plot(
            #     path_w,
            #     path_b,
            #     [loss_function(x_data, y_data, path_w[i], path_b[i])
            #      for i in range(len(path_w))],
            #     c="r"
            # )



        plt.pause(1)
