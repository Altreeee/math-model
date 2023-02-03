from sklearn.decomposition import FactorAnalysis
import numpy as np
import pandas as pd


data = pd.read_excel('tidy.xlsx')

# 将流派名称转换为数字
data["Genre"] = data["Genre"].astype('category')
data["Genre_num"] = data["Genre"].cat.codes

# 因子分析
fa = FactorAnalysis(n_components=3)
data_transformed = fa.fit_transform(data.iloc[:, 2:9])

# 提取最重要的3个因子
data_transformed = data_transformed[:, :3]

# 将因子数据和原数据合并
data_transformed = np.hstack([data_transformed, data.iloc[:, [0, 9]]])
result_df = pd.DataFrame(data_transformed, columns=['Factor 1', 'Factor 2', 'Factor 3', 'Genre', 'Genre_num'])
result_df.to_excel('result.xlsx', index=False)

