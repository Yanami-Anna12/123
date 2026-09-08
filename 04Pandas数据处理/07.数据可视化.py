""""""
"""
plot 绘制可视化图标, 又灵活的接口
"""

import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 2, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s.plot(kind='line', title='Line Plot', grid=True, figsize=(8, 4), style='r--', linewidth=2)
plt.show()
