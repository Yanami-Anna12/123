# Pandas 功能模块表

| 功能模块 | 功能点 | 功能简介 | 功能详情 | 补充说明 |
| --- | --- | --- | --- | --- |
| Series 创建 | 用标量创建 | 用单个值创建，数据沿指定索引自动重复填充 | pd.Series(5, index=['a', 'b', 'c'], name='test', dtype=np.float64) | name 设置名称，dtype 指定数据类型 |
| Series 创建 | 用列表创建 | 由序列数据创建，不指定时自动生成 0 到 n-1 的位置索引 | pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 1, 2, 3]) | 自定义 index 标签数量需不少于数据个数，不足部分以 NaN 填充 |
| Series 创建 | 用字典创建 | 由键值对创建，字典键默认作为索引 | pd.Series({'a': 1, 'b': 2, 'c': 3}) | 一般不再另设 index；指定后字典中不存在的键对应 NaN |
| Series 创建 | 用 ndarray 创建 | 由 NumPy 数组创建并指定索引 | pd.Series(np.array([1, 2, 3, 4, 5]), index=[...], copy=False) | copy=False 时不复制原数据，修改 Series 会连带修改原数组 |
| Series 属性 | 索引与数据 | 获取或重设索引、取出数据值 | 使用 ser.index、ser.values（数据以 ndarray 返回） | ser.index 支持整体重新赋值，如 ser.index = ['a','b','c'] |
| Series 属性 | 结构信息 | 查看数据类型、形状、元素个数、维度、占用字节数 | dtype/dtypes、shape、size、ndim、nbytes | 便于了解数据规模与内存占用 |
| Series 属性 | 状态判断 | 判断是否为空、含 NaN、元素唯一、单调递增/递减 | empty、hasnans、is_unique、is_monotonic_increasing、is_monotonic_decreasing | 均返回布尔值 |
| Series 属性 | 其他属性 | 查看底层数组、轴标签，附加说明信息 | array、axes、attrs | attrs 可赋字典，存放来源、时间等说明性元数据 |
| Series 索引访问 | 位置与标签索引 | 按位置编号或标签获取元素 | 使用 ser[1]（位置）、ser['a']（标签） | 标签重复时返回满足条件的全部元素 |
| Series 索引访问 | 切片访问 | 截取一段连续数据 | 位置切片 ser[0:3]（左闭右开）；标签切片 ser['a':'c']（左闭右闭） | 两种切片含不含末尾元素的规则不同，需注意区分 |
| Series 索引访问 | loc 与 iloc | 用更明确的索引方式访问数据 | ser.loc['a'] 按标签取、ser.iloc[0:2] 按位置取 | 显式索引，写法清晰，推荐优先使用 |
| Series 索引访问 | 常用访问方法 | 快速查看或筛选数据 | head(n)/tail(n) 查看头尾、isin(列表) 判断元素是否在其中、get(key, default) 安全取值、at/iat 访问单个元素 | head 默认返回前 5 行；get 找不到标签时返回 default（默认 None） |
