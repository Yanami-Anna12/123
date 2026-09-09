import math
import numpy as np

"""
============================================================
                    常用距离度量函数库
============================================================
"""


# ============ 1. 欧氏距离（Euclidean Distance） ============
def euclidean_distance(x, y):
    """
    两点之间的直线距离，最常用
    公式: sqrt(sum((x_i - y_i)^2))
    """
    return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))


# ============ 2. 曼哈顿距离（Manhattan Distance） ============
def manhattan_distance(x, y):
    """
    坐标差的绝对值之和，类似城市街区距离
    公式: sum(|x_i - y_i|)
    """
    return sum([abs(a - b) for a, b in zip(x, y)])


# ============ 3. 切比雪夫距离（Chebyshev Distance） ============
def chebyshev_distance(x, y):
    """
    坐标差的最大值，类似棋盘上国王移动的距离
    公式: max(|x_i - y_i|)
    """
    return max([abs(a - b) for a, b in zip(x, y)])


# ============ 4. 闵可夫斯基距离（Minkowski Distance） ============
def minkowski_distance(x, y, p):
    """
    欧氏距离和曼哈顿距离的广义形式
    p=1 时为曼哈顿距离，p=2 时为欧氏距离
    公式: (sum(|x_i - y_i|^p))^(1/p)
    """
    if p <= 0:
        raise ValueError("p 必须大于 0")
    # p 值过大时用对数方式避免溢出
    if p > 100:
        return minkowski_distance_log(x, y, p)
    return sum([abs(a - b) ** p for a, b in zip(x, y)]) ** (1 / p)


def minkowski_distance_log(x, y, p):
    """
    用对数方式计算闵可夫斯基距离，避免 p 很大时数值溢出
    """
    values = [abs(a - b) for a, b in zip(x, y)]
    max_val = max(values)
    if max_val == 0:
        return 0.0
    log_sum = sum([p * math.log(v / max_val) for v in values if v > 0])
    return max_val * math.exp(log_sum / p)


# ============ 5. 余弦相似度（Cosine Similarity） ============
def cosine_similarity(x, y):
    """
    计算两个向量的夹角余弦值，值越接近1表示方向越一致
    公式: (x·y) / (||x|| * ||y||)
    """
    dot_product = sum([a * b for a, b in zip(x, y)])
    norm_x = math.sqrt(sum([a ** 2 for a in x]))
    norm_y = math.sqrt(sum([b ** 2 for b in y]))
    if norm_x == 0 or norm_y == 0:
        return 0.0
    return dot_product / (norm_x * norm_y)


def cosine_distance(x, y):
    """
    余弦距离 = 1 - 余弦相似度，值越小越相似
    """
    return 1 - cosine_similarity(x, y)


# ============ 6. 汉明距离（Hamming Distance） ============
def hamming_distance(x, y):
    """
    两个等长序列对应位置不同元素的个数
    通常用于文本比较、编码错误检测
    """
    if len(x) != len(y):
        raise ValueError("两个序列长度必须相等")
    return sum([1 for a, b in zip(x, y) if a != b])


# ============ 7. 杰卡德相似度/距离（Jaccard） ============
def jaccard_similarity(set_x, set_y):
    """
    集合交集大小 / 集合并集大小
    值越大表示两个集合越相似
    """
    if not set_x and not set_y:
        return 1.0
    intersection = len(set_x.intersection(set_y))
    union = len(set_x.union(set_y))
    return intersection / union if union != 0 else 0


def jaccard_distance(set_x, set_y):
    """
    杰卡德距离 = 1 - 杰卡德相似度
    """
    return 1 - jaccard_similarity(set_x, set_y)


# ============ 8. 马氏距离（Mahalanobis Distance） ============
def mahalanobis_distance(x, y, cov_inv):
    """
    考虑数据协方差矩阵的距离，消除量纲影响
    需要传入协方差矩阵的逆矩阵
    公式: sqrt((x-y)^T * S^(-1) * (x-y))
    """
    diff = np.array(x) - np.array(y)
    # 确保 diff 是列向量
    return math.sqrt(diff.T @ cov_inv @ diff)


# ============ 9. 半正矢距离（Haversine Distance） ============
def haversine_distance(lat1, lon1, lat2, lon2, radius=6371.0):
    """
    计算地球表面两点之间的球面距离（大圆距离）

    参数:
        lat1, lon1: 第一个点的纬度和经度（单位：度）
        lat2, lon2: 第二个点的纬度和经度（单位：度）
        radius: 球体半径，默认 6371.0 公里（地球平均半径）
                也可以传入 3956.0 得到英里

    返回:
        两点之间的球面距离（单位与 radius 一致）
    """
    # 将角度转换为弧度
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # 纬度差和经度差
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # 半正矢公式
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return radius * c


# ============================================================
#                        测试代码
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("                    距离计算测试")
    print("=" * 60)

    # 测试数据
    x = [1, 2, 3]
    y = [4, 5, 6]
    print(f"向量 x = {x}")
    print(f"向量 y = {y}")
    print("-" * 60)

    # 1. 欧氏距离
    print(f"1. 欧氏距离:                       {euclidean_distance(x, y):.6f}")

    # 2. 曼哈顿距离
    print(f"2. 曼哈顿距离:                     {manhattan_distance(x, y):.6f}")

    # 3. 切比雪夫距离
    print(f"3. 切比雪夫距离:                   {chebyshev_distance(x, y):.6f}")

    # 4. 闵可夫斯基距离
    print(f"4. 闵可夫斯基距离 (p=1):           {minkowski_distance(x, y, 1):.6f}")
    print(f"  闵可夫斯基距离 (p=2):           {minkowski_distance(x, y, 2):.6f}")
    print(f"  闵可夫斯基距离 (p=3):           {minkowski_distance(x, y, 3):.6f}")
    print(f"  闵可夫斯基距离 (p=2000000):     {minkowski_distance(x, y, 2000000):.6f}")

    # 5. 余弦相似度/距离
    print(f"5. 余弦相似度:                     {cosine_similarity(x, y):.6f}")
    print(f"  余弦距离:                       {cosine_distance(x, y):.6f}")

    # 6. 汉明距离
    print(f"6. 汉明距离 ([1,2,3] vs [1,5,3]): {hamming_distance([1, 2, 3], [1, 5, 3])}")

    # 7. 杰卡德距离
    set_a = {1, 2, 3, 4}
    set_b = {3, 4, 5, 6}
    print(f"7. 杰卡德相似度 ({set_a} vs {set_b}): {jaccard_similarity(set_a, set_b):.4f}")
    print(f"  杰卡德距离:                     {jaccard_distance(set_a, set_b):.4f}")

    # 8. 马氏距离
    cov_inv_example = np.linalg.inv([[1, 0.5], [0.5, 1]])
    print(f"8. 马氏距离:                       {mahalanobis_distance([1, 2], [3, 4], cov_inv_example):.6f}")

    # 9. 半正矢距离（球面距离）
    beijing = (39.9042, 116.4074)
    shanghai = (31.2304, 121.4737)
    distance_km = haversine_distance(beijing[0], beijing[1], shanghai[0], shanghai[1])
    distance_miles = haversine_distance(beijing[0], beijing[1], shanghai[0], shanghai[1], radius=3956.0)
    print(f"9. 半正矢距离 (北京→上海):          {distance_km:.2f} 公里")
    print(f"                                    {distance_miles:.2f} 英里")

    print("=" * 60)