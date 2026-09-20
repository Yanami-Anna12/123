import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gsp

points = np.array([[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4,-15.7], [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6], [0.4, 34.0], [0.8, 62.3]])
X = points[:, 0]
Y = points[:, 1]

w = 0
b = -1
lr = 0.01

def loss_func(X, w, b):
    pre_y = np.dot(X, w) + b
    total_loss = np.mean((pre_y - Y) ** 2)
    return total_loss

def SGD(points, w, b, lr, batch_size):
    np.random.shuffle(points)
    for num_batch in range(0, len(points), batch_size):
        batch_points = points[num_batch:num_batch+batch_size, :]
        batch_x = batch_points[:, 0]
        batch_y = batch_points[:, 1]

        batch_pre_y = w * batch_x + b
        dw = np.mean(2 * (batch_pre_y - batch_y) * batch_x)
        db = np.mean(2 * (batch_pre_y - batch_y))

        w -= lr * dw
        b -= lr * db
    return w, b

w_values = np.linspace(-20, 80, 100)
b_values = np.linspace(-20, 80, 100)
W, B =np.meshgrid(w_values, b_values)
loss_values = np.zeros_like(W)

for i, w in enumerate(w_values):
    for j, b in enumerate(b_values):
        loss_values[j, i] = loss_func(X, w, b)

fig =  plt.figure(figsize=(12, 6))
gs = gsp.GridSpec(2, 2)
ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot((gs[1, 0]))
ax3 = fig.add_subplot(gs[:, 1], projection='3d')
ax3.plot_surface(W, B, loss_values, cmap='viridis', alpha=0.8)

gd_path = []

epoches = 1000
bs = 10
for epoch in range(1, epoches+1):
    gd_path.append((w, b))
    w, b = SGD(points, w, b, lr, batch_size=bs)
    if epoch == 1 or epoch % 20 == 0:
        print(loss_func(X, w, b))
        ax1.clear()
        ax1.scatter(X, Y, c='r')
        x_line = np.linspace(np.min(X), np.max(X), 2)
        y_line = np.dot(x_line, w) + b
        ax1.plot(x_line, y_line, c='g')

        ax2.clear()
        ax2.contourf(W, B, loss_values, levels=50, cmap='viridis')
        ax2.scatter(w, b, c='black', s=20)
        gd_w, gd_b = zip(*gd_path)
        ax2.plot(gd_w, gd_b, c='black')

        ax3.scatter(w, b, loss_func(X, w, b), c='black', s=20)
        ax3.plot(gd_w, gd_b, [loss_func(X, gd_w[i], gd_b[i]) for i in range(len(gd_w))], c='black')

        plt.pause(0.3)
plt.show()