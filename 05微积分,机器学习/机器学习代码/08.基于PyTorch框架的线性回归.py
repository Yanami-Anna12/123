import torch
import torch.nn as nn
import numpy as np

# 随机数种子,确保每次运行时,生成的随机数是相同的
# seed = 42
# torch.margin_ranking_loss(seed)
#
# random_tesor = torch.rand((3, 4))
# print(random_tesor)

data = [[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4, -15.7], [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6], [0.4, 34.0], [0.8, 62.3]]

data = np.array(data)

x_data = data[:, 0]
y_data = data[:, 1]

x_train = torch.tensor(x_data, dtype=torch.float32)
y_train = torch.tensor(y_data, dtype=torch.float32)

# 设置随机种子
seed = 42
torch.manual_seed(seed)


# 定义一个线性层（模型） y = wx + b
model = nn.Linear(1, 1)

# 1) nn.Sequential 是pytorch的一个模块容器
# forward 方法会定义模型的前向传播逻辑,有序, nn.Sequential默认自带
# model = nn.Sequential(nn.Linear(1, 1))

# 2) nn.ModuleList
# 默认无forward
# class LinearModel(nn.Module):
#     def __init__(self):
#         super(LinearModel, self).__init__()
#         self.layers = nn.ModuleList([nn.Linear(1, 1)])
#
#     def forward(self, x):
#         for layer in self.layers:
#             x = layer(x)
#         return x
#
# model = LinearModel()


# 3) nn.ModuleDict
# 可以给每个层自定义名字
# class LinearModel(nn.Module):
#     def __init__(self):
#         super(LinearModel, self).__init__()
#         self.layers = nn.ModuleDict({"linear": nn.Linear(1, 1)})
#
#     def forward(self, x):
#         for layer in self.layers.values():
#             x = layer(x)
#         return x
# model = LinearModel()

"""
最常用的方案
"""
# class LinearModel(nn.Module):
#     def __init__(self):
#         super(LinearModel, self).__init__()
#         self.linear = nn.Linear(1, 1)
#         self.linear2 = nn.Linear(2, 1)
#
#     def forward(self, x):
#         x = self.linear(x)
#         return x
# model = LinearModel()


# 定义损失函数为均方误差
criterion = nn.MSELoss()

# 定义优化器为随机梯度下降
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

epoches = 500
for n in range(1, epoches+1):
    y_hat = model(x_train.unsqueeze(1))
    loss = criterion(y_hat, y_train.unsqueeze(1))
    # 清空存储在优化器中的梯度
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if n % 10 == 0 or n == 1:
        print(f"epoches:{n}, loss:{loss}")