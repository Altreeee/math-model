#利用influence_data统计所有艺术家及其人名
#产生NUM_GENRE：最终结果2，所有音乐家的流派和人名

import pandas as pd

# 读取表格
data = pd.read_excel('quoi.xlsx')

# 创建一个新的表格
people_data = pd.DataFrame(columns=['ID', '人名', '流派', '年份'])

# 遍历所有的人
for i in range(data.shape[0]):
    
        # 获取这个人的数据
        name = data.iloc[i, 0]
        age = data.iloc[i, 1]
        gender = data.iloc[i, 2]
        address = data.iloc[i, 3]
        
        if people_data[people_data['ID'] == name].empty:
            people_data = people_data.append({'ID': name, '人名': age, '流派': gender, '年份': address}, ignore_index=True)
        
        # 添加第4，5，6，7列中的人
        name = data.iloc[i, 4]
        age = data.iloc[i, 5]
        gender = data.iloc[i, 6]
        address = data.iloc[i, 7]
        
        if people_data[people_data['ID'] == name].empty:
            people_data = people_data.append({'ID': name, '人名': age, '流派': gender, '年份': address}, ignore_index=True)



# 将结果保存到新的表格中
people_data.to_excel('NUM_GENRE.xlsx', index=False)
