import torch
# # 打印一个标量
# scalar_tensor = torch.tensor(3.14)
# print("scalar_tensor:", scalar_tensor)
#
# # 打印一个向量
# vector_tensor = torch.tensor([1, 2, 3, 4, 5, 6])
# print("vector_tensor:", vector_tensor)
#
# # 打印一个矩阵
# matrix_tensor = torch.tensor([[1, 2], [3, 4]])
# print("matrix_tensor:", matrix_tensor)

"""
tensor的存储
# """
# tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
# print(tensor1)
# # 打印形状
# print(tensor1.shape)
# # 数据类型
# print(tensor1.dtype)
# # 存储内容
# print(tensor1.storage())

"""
storage的存储
"""
# a = torch.arange(12).reshape(3, 4)
# print(a)
# print(a.storage().tolist())
# print(a.storage().data_ptr())
#
# b = a.transpose(0, 1)
# print(b)
# print(b.storage().tolist())
# print(b.storage().data_ptr())

"""
tensor的步长
"""
# a = torch.arange(12).reshape(3, 4)
# print(a)
# print(a.stride())  # (4, 1) 表示底层需要走4步, 表层走1步到达


"""
tensor的连续性
"""
a = torch.arange(12).reshape(3, 4)
print(a.flatten())
print(a.storage().tolist())
b = a.transpose(0, 1)
print(b.flatten())
print(b.storage().tolist())
# print(b.view(1, 12))    #RuntimeError: view size is not compatible with input tensor's size and stride (at least one dimension spans across two contiguous subspaces). Use .reshape(...) instead.
print(b.is_contiguous())
# 使用 contiguous 处理不连续的张量, 会为不连续的张量重新开辟一块内存空间保证数据在内存中是连续的
b = b.contiguous()
print(b.view(1, 12))