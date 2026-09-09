import time

import numpy as np
import matplotlib.pyplot as plt
from sympy.physics.vector import gradient

point = [[0.8,1.0],[1.7,0.9],[2.7,2.4],[3.2,2.9],[3.7,2.8],[4.2,3.8],[4.2,2.7]]

data = np.array(point)

x_data = data[:, 0]     # 拿到所有的x
y_data = data[:, 1]     # 拿到所有的y

# y = wx + b
w = 10
w_old = w
b = 0
y_hat = w * x_data + b
learning_rate = 0.01

e = y_data - y_hat
print("单点误差e:", e)
# 方差
e_bar = np.mean(e ** 2)

fig = plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

# step = 10
# for i in range(step):
while 1:
    # w_old所在点的切线斜率, 通过对e_bar与w的函数求导而来
    gradient = 2 * w_old * np.mean(x_data ** 2) - 2 * np.mean(x_data * y_data)
    if np.abs(gradient) >= 0.1:
        ax1.cla()
        ax2.cla()
        # w_new = w_old - 固定值 * 斜率
        w_new = w_old - learning_rate * gradient
        y_hat_new = w_new * x_data + b
        e_bar_new = np.mean((y_hat_new - y_data) ** 2)
        print(e_bar_new)

        ax1.set_xlim(0, 5)
        ax1.set_ylim(0, 6)
        ax1.set_xlabel("x axis label")
        ax1.set_ylabel("y axis label")
        ax1.scatter(x_data, y_data, color='b')
        y1 = w_new * 0 +b
        y2 = w_new * 5 +b
        ax1.plot([0, 5], [y1, y2], color='r', linewidth=3)

        for x, y_true, y_pre in zip(x_data, y_data, y_hat_new):
            ax1.plot([x, x], [y_true, y_pre], color='g', linestyle='--')


        w_values = np.linspace(0, 3, 100)
        e_values = [np.mean((y_data - (w_value * x_data + b)) ** 2) for w_value in w_values]
        ax2.plot(w_values, e_values, color='g', linewidth=3)
        ax2.plot(w_new, e_bar_new, marker='o', color='r')
        ax2.set_xlabel("w axis label")
        ax2.set_ylabel("e axis label")
        plt.pause(0.2)
        w_old = w_new

    else:
        break

plt.show(block=False)
time.sleep(3)