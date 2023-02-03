# 调用一个名为“data.xls”表格，
# 其每一行依次是一个人名、他的流派、他的追随者数、年份。
# 得到一个图，其中y轴是每个流派的追随者人数，x轴是时间，每种流派画一条曲线。


import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_excel('data_1.xlsx')

# 按流派和年份分组，并计算追随者数之和
groups = data.groupby(['流派', '年份'])['追随者数'].sum().reset_index()
                    #产生一个行列分别为流派和年份的二位数组
                                    #统计每组数据中追随者数的和
                                                        #将统计值转换为Dataframe,分别对应'流派'，'年份'，'追随者数' 。

# 创建一个图形
fig, ax = plt.subplots()

# 循环每一个流派，绘制曲线
for name, group in groups.groupby('流派'):
    ax.plot(group['年份'], group['追随者数'], label=name)

# 添加图例
ax.legend()

# 显示图形
plt.show()

