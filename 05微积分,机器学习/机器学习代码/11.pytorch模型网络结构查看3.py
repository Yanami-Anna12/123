import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import DataLoader, TensorDataset
from tensorboardX import SummaryWriter as SummaryWriter

data = [[-0.5, 7.7], [1.8, 98.5], [0.9, 57.8], [0.4, 39.2], [-1.4, -15.7], [-1.4, -37.3], [-1.8, -49.1], [1.5, 75.6], [0.4, 34.0], [0.8, 62.3]]

data = np.array(data)

x_data = data[:, 0]
y_data = data[:, 1]

x_train = torch.tensor(x_data, dtype=torch.float32)
y_train = torch.tensor(y_data, dtype=torch.float32)

# 用于封装张量, 将输入张量和目标张量组成一个数据集
dataset = TensorDataset(x_train, y_train)


# 设置随机种子
seed = 42
torch.manual_seed(seed)


# 定义一个线性层（模型） y = wx + b

"""
最常用的方案
"""
class LinearModel(nn.Module):
    def __init__(self):
        super(LinearModel, self).__init__()
        self.linear = nn.Linear(1, 1)
        self.linear2 = nn.Linear(2, 1)

    def forward(self, x):
        x = self.linear(x)
        return x
model = LinearModel()


# 定义损失函数为均方误差
criterion = nn.MSELoss()

# 定义优化器为随机梯度下降
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

epoches = 500

dataloader = DataLoader(dataset, batch_size=10, shuffle=True)

# 创建对象
writer = SummaryWriter(log_dir='logs')

for n in range(1, epoches+1):
    total_loss = 0
    for batch_x, batch_y in dataloader:
        y_hat = model(x_train.unsqueeze(1))
        loss = criterion(y_hat, y_train.unsqueeze(1))
        total_loss += loss
        # 清空存储在优化器中的梯度
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # 计算平均损失
    avg_loss = total_loss / len(dataloader)

    writer.add_scalar('Loss', avg_loss, n)
    writer.add_scalar('learning_rate', optimizer.param_groups[0]['lr'], n)


    if n % 10 == 0 or n == 1:
        print(f"epoches:{n}, loss:{avg_loss}")

# 将计算图添加到writer中
writer.add_graph(model, torch.rand(1))
writer.close()