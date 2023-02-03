import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('NUM_GENRE.xlsx')

# 按流派分组NUM_GENRE
groups = data.groupby(['流派','年份']).size().reset_index(name='num')

groups.to_excel('1_2_1.xlsx',index=False)