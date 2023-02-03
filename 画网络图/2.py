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

#用influence_data连线
#第二列是influencer,第六列是follower,要去掉第一行
influencer_data=[]
follower_data=[]
for s in wc.sheets():
    for row in range(s.nrows):
        values = []
        if row >= 1 and row<1000:
            for col in range(s.ncols):
                values.append(s.cell(row,col).value)
            '''print (values)              #values是存行的数列'''
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
#读入追随者数量的表格
follower_count = pd.read_excel("follower_count.xlsx")
#存入字典
follower_dict = dict(zip(follower_count["Name"], follower_count["Follower Count"]))

for i in range(len(follower_data)):
    G.nodes[follower_data[i]]['size'] = follower_dict.get(follower_data[i], 0)
    G.nodes[influencer_data[i]]['size'] = follower_dict.get(influencer_data[i], 0)
    G.nodes[follower_data[i]]['color'] = "blue"
    G.nodes[influencer_data[i]]['color'] = "red"


'''pos = nx.kamada_kawai_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=[d['size'] for v, d in G.nodes(data=True)], node_color=[d['color'] for v, d in G.nodes(data=True)])
nx.draw_networkx_edges(G, pos, alpha=0.3)
                                #透明度
nx.draw_networkx_labels(G, pos, labels={n:'' for n in G.nodes()})
                                #去掉人名，显示人名就把这里删掉
plt.show()'''

#上面是画全体网络图的，下面是画名为“X”的节点的深度为2的子网络图的，上下按需取其一

'''subgraph = nx.ego_graph(G, 'X', radius=2)  #深度为2，提取名为X点的网络
#画子网络
pos = nx.kamada_kawai_layout(G)
nx.draw_networkx_nodes(subgraph, pos, node_size=[d['size'] for v, d in subgraph.nodes(data=True)], node_color=[d['color'] for v, d in subgraph.nodes(data=True)])
nx.draw_networkx_edges(subgraph, pos, alpha=0.3)
                                #透明度
nx.draw_networkx_labels(subgraph, pos, labels={n:'' for n in subgraph.nodes()})
                                    #去掉人名，显示人名就把这里删掉
plt.title('Sub-network of Umples')
plt.show()'''
