#横轴还是时间，纵轴是流派内的艺术家数
#使用NUM_GENRE.xlsx 相对于csv格式数据改动了一下最上方的列命名

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('NUM_GENRE.xlsx')

# 按流派分组NUM_GENRE
groups = data.groupby(['流派','年份']).size().reset_index(name='num')

# 创建一个图形
fig, ax = plt.subplots()

# 循环每一个流派，绘制曲线
for name, group in groups.groupby(['流派']):
    ax.plot(group['年份'], group['num'], label=name)

# 添加图例
ax.legend()

# 显示图形
plt.show()