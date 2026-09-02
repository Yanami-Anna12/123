import numpy as np

# 1.1 创建ndarray对象
print("==========创建ndarray对象===========")
arr1 = np.arange(15).reshape(3,5)
print(arr1)
print('hello')

# 1.2 常用属性
print("==========常用属性===========")
print(f'numpy的轴:{arr1.ndim}')
print(f'numpy的维度:{arr1.shape}')
print(f'numpy的元素类型:{arr1.dtype}')
print(f'numpy的元素个数:{arr1.size}')
print(f'numpy的元素占用字节数:{arr1.itemsize}')

# 2 创建numpy的ndarray对象
## 2.1 array()函数
print("=====================")
my_list = [11, 22, 33, 44, 55]
print(type(my_list))
arr2 = np.array(my_list)
print(arr2,type(arr2))

## 2.2 arange()函数
# arange(起始, 结束, 步长, dtype=类型)
print("=====================")
arr3 = np.arange(0, 10, 2)
print(arr3, type(arr3), arr3.dtype)

## 2.3 随机数生成 ndaary 对象
print("==========随机数生成 ndaary 对象===========")
arr4 = np.random.rand(3, 5) # 3行5列
print(arr4)

arr5 = np.random.randint(3, 9, size=(2, 6)) # 3~9,2行6列
print(arr5)

arr6 = np.random.uniform(3, 9, size=(2, 6))
print(arr6)

## 2.4 numpy 的类型转换
print("==========numpy 的类型转换===========")
arr7 = np.arange(0, 10, 2, dtype=np.int64)
print(arr7, arr7.dtype)
arr8 = arr7.astype(np.float32)
print(arr8, arr8.dtype)

## 2.5 等比数列
print("==========等比数列===========")
arr9 = np.logspace(0, 3, 3, base=10) # 10^0 开始, 10^3 结束, 共3个数 , base 默认是10
print(arr9, arr9.dtype)

## 2.6 等差数列
print("==========等差数列===========")
arr10 = np.linspace(0, 12, 4, endpoint=False, dtype=np.float64)
print(arr10, arr10.dtype)

# 3 numpy的常用函数
## 3.1 标准的正态分布
print("==========标准的正态分布===========")
arr1 = np.random.randn(3, 5)
print(arr1)
print("向上取整\n",np.ceil(arr1))        # 向上取整
print("向下取整\n",np.floor(arr1))       # 向下取整
print("四舍五入\n",np.rint(arr1))        # 四舍五入
print("绝对值\n",np.abs(arr1))         # 绝对值
print("乘法\n",np.multiply(arr1, arr1))  # 乘法 同 arr1 * arr1
print("除法\n",np.divide(arr1, arr1))    # 除法
print("类似三元\n",np.where(arr1 > 0, 1, -1))  # 类似三元

## 3.2 统计函数
print("==========统计函数===========")
arr = np.arange(12).reshape(3, 4)
print(arr)
print(np.cumsum(arr))       # 累加和
print(np.sum(arr))          # 和
print(np.sum(arr, axis=0))  # 列求和
print(np.sum(arr, axis=1))  # 行求和

## 3.3 去重函数
print("=========去重函数============")
arr = np.array([[1, 2, 1], [2, 3, 5]])
print(arr)
arrr = np.unique(arr)   # 原始未变
print(arrr)

## 3.4 排序函数
print("==========排序函数===========")
arr = np.array([1, 6, 3, 2, 5])
print(arr)
print(np.sort(arr))     # 原始未变
arr.sort()              # 原始变化
print(arr)

# 4 矩阵运算
## 4.1 加减
print("==========加减===========")
arr = np.array([10, 20, 30, 40])
arrr = np.arange(4)
print(arr,arrr)
print(arr - arrr)
print(arr + arrr)

## 4.2 矩阵乘法
print("==========矩阵乘法===========")
arr1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(np.dot(arr1, arr2))
print(arr1.dot(arr2))
print(arr1 @ arr2)