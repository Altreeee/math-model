import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('merged_data_blues.xlsx')

# 按年份分组计算每年歌曲popularity的均值
groups = data.groupby(['year'])['popularity'].mean().reset_index(name='popularity_mean')

# 创建图形
fig, ax = plt.subplots()

# 绘制图形
ax.plot(groups['year'], groups['popularity_mean'])

# 设置标题、x轴标签、y轴标签
ax.set(title='Mean Popularity of Songs by Year', xlabel='Year', ylabel='Mean Popularity')

# 显示图例
ax.legend(['Songs'])

# 显示图形
plt.show()
