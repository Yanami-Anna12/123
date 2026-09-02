# NumPy 功能模块表

| 功能模块 | 功能点 | 功能简介 | 功能详情 | 补充说明 |
| --- | --- | --- | --- | --- |
| ndarray 创建 | 多种创建方式 | 掌握生成 NumPy 数组的常用方法 | 包括 array()、arange()、random.rand()、random.randint()、random.uniform()、logspace()、linspace() | 可指定 dtype，支持 reshape 改变形状 |
| ndarray 属性 | 查看数组属性 | 获取数组的轴数、形状、元素类型、大小、字节数 | 使用 ndim、shape、dtype、size、itemsize | 便于调试和内存优化 |
| 类型转换 | 修改元素数据类型 | 将数组元素类型转为指定类型 | 使用 astype() 转为 np.float32、np.int64 等 | 不影响原数组，返回新数组 |
| 随机数生成 | 生成随机数组 | 生成均匀分布、正态分布、整数随机数 | rand()、randn()、randint()、uniform() | 支持指定 size 和范围 |
| 数学与取整运算 | 对数组元素进行数学操作 | 包括向上/向下取整、四舍五入、绝对值、乘除法 | ceil()、floor()、rint()、abs()、multiply()、divide() | 支持逐元素运算 |
| 条件判断 | where 条件筛选 | 根据条件返回不同值，类似三元运算符 | np.where(arr > 0, 1, -1) | 支持复杂条件组合 |
| 统计函数 | 求和与累加 | 计算数组总和、行/列求和、累加和 | sum()、cumsum()，支持 axis=0/1 | axis=0 为列，axis=1 为行 |
| 去重函数 | 去除重复元素 | 返回数组中唯一值，支持多维展平 | np.unique() | 不修改原数组 |
| 排序函数 | 数组排序 | 升序排序，支持原地排序或返回新数组 | np.sort()（返回新）、arr.sort()（原地） | 默认按最后一个轴排序 |
| 矩阵运算 | 矩阵加减法 | 相同形状数组逐元素加减 | 直接用 +、- 操作 | 需形状一致或满足广播规则 |
| 矩阵运算 | 矩阵乘法 | 实现点积/矩阵乘 | 使用 dot() 或 @ 运算符进行矩阵乘法（np.dot(arr1, arr2)、arr1.dot(arr2)、arr1 @ arr2） | 左列数需等于右行数 |
