import torch
import torch.nn as nn
import numpy as np
from torch.utils.data import DataLoader, TensorDataset
from torchsummary import summary

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

    def forward(self, x):
        x = self.linear(x)
        return x
model = LinearModel()


# 保存模型
# torch.save(model.state_dict(), 'model.pth')
# model.load_state_dict(torch.load('model.pth'))
# # 评估模型
# model.eval()

# 保存模型的结构与参数
torch.save(model, 'data/entire_model.pth')
entire_model = torch.load('data/entire_model.pth', weights_only=False)
entire_model.eval()

# 使用模型进行一些预测
x_test = torch.tensor([[1.2], [3.4]], dtype=torch.float32)
with torch.no_grad():
    y_pred = entire_model(x_test)
print(y_pred)

# 直接打印模型并不能检测模型搭建是否正确
print(model)

# summary 能检测模型搭建是否正确, 打印设备默认是CUDA(GPU) RuntimeError: mat1 and mat2 shapes cannot be multiplied (2x1 and 2x1)
# print(summary(model, (1, )))