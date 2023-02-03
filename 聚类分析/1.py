#使用聚类算法将流派按照不同的音乐要素分类，以找出流派之间在音乐要素上的联系
#重新做一个xlsx表格，流派+音乐要素，音乐要素就用A，B，C，D来命名吧
#新的整理表格的要素顺序都是和merged_data.xlsx一样的

import pandas as pd
from sklearn.cluster import KMeans

data=pd.read_excel("data.xlsx")

data_1=data[["A","B","C","D","E","F","G"]]
data_2=data[["H","Y","J","K"]]
#data_3=data[["L","M"]]

kmeans = KMeans(n_clusters=4)   #应该聚几类呢？

kmeans.fit(data_1)
clusters = kmeans.predict(data_1)
data_1=data_1.assign(clusters=clusters)
data_1.to_excel("data_1_with_clusters.xlsx",index=False)

kmeans.fit(data_2)
clusters = kmeans.predict(data_2)
data_2=data_2.assign(clusters=clusters)
data_2.to_excel("data_2_with_clusters.xlsx",index=False)

'''kmeans.fit(data_3)
clusters = kmeans.predict(data_3)
data_3=data_3.assign(clusters=clusters)
data_3.to_excel("data_3_with_clusters.xlsx",index=False)'''
