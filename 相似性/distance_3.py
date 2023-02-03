import pandas as pd
from scipy.spatial import distance
import numpy as np
from numpy import *

def calEuclideanDistance(vec1,vec2):
    dist = np.sqrt(np.sum(np.square(vec1-vec2)))
    return dist

# 读取xlsx表格
df = pd.read_excel("try_2.xlsx")

# 计算每两种音乐流派之间的距离
distances = {}
##df.index = range(len(df))

for i in range(len(df)):
    for j in range(i+1, len(df)):

            genre1, genre2 = df.iloc[i,3], df.iloc[j,3]
            feature1, feature2 = df.iloc[[i],[0,1,2]], df.iloc[[j],[0,1,2]]
            ##将列表变为向量
            feature1=np.array(feature1)
            feature2=np.array(feature2)
            genre1=str(genre1)
            genre2=str(genre2)
            dist = calEuclideanDistance(feature1, feature2)


            #如果在字典的键中已经有同样的两个流派但是只是顺序相反时，就将现在的改变成已有的键

            if (genre2,genre1) in distances:
                k = genre1
                genre1 = genre2
                genre2 = k

            distances.setdefault((genre1, genre2), []).append(dist)


# 将距离存放在新表格中
data = []
for key, value in distances.items():
    v=sum(value)/len(value)
    data.append([key[0], key[1], v])
df_dist = pd.DataFrame(data, columns=['genre1', 'genre2', 'distance'])  #distance是平均值


# 将结果写入新表格
'''
df_distance = df_dist.join(df_dist.pop('distance').apply(pd.Series))
df_distance.columns = ['genre1', 'genre2'] + [f'distance_{i}' for i in range(df_distance.shape[1]-2)]
df_distance.to_excel("distances.xlsx")
'''
df_dist.to_excel("distances_2.xlsx",index=False)

