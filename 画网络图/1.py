#2021D第一题画图，影响者与被影响者网络图
#2023，1，6


import matplotlib.pyplot as plt
import xlrd
from xlrd import open_workbook
import networkx as nx
import pandas as pd
import numpy as np

G=nx.Graph()

#读取excel表格
#不支持xlsx格式了，要另存一下为xls
wc = open_workbook('influence_data.xls')
 
'''
x_data=[]
for s in wb.sheets():
    for row in range(s.nrows):
        print ('the',row,'row is:')
        values = []
        for col in range(s.ncols):
            values.append(s.cell(row,col).value)
        print (values)              #values是存行的数列
        x_data.append(values[0])    #x_data是表格第一列
#x_data是所有艺术家名字
'''

#用influence_data连线
#第二列是influencer,第六列是follower,要去掉第一行
influencer_data=[]
follower_data=[]
for s in wc.sheets():
    for row in range(s.nrows):
        print ('the',row,'row is:')
        values = []
        if row >= 1 and row<100:
            for col in range(s.ncols):
                values.append(s.cell(row,col).value)
            print (values)              #values是存行的数列
            influencer_data.append(values[1])    #deux_data是表格第二列
            follower_data.append(values[5])

#配对成[follower，influencer]，建立有向边
edges=pd.DataFrame()
edges['sources']=follower_data  #有向边的起点
edges['targets']=influencer_data    #有向边的终点
edges['weights']=np.ones(len(follower_data))
G=nx.from_pandas_edgelist(
    edges,
    source='sources',
    target='targets',
    edge_attr='weights'
)
nx.draw(G,with_labels=True)#with_labels：节点是否带标签
plt.show()