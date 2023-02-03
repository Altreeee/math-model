#将data_by_artist和NUM_GENRE合并起来
'''
import pandas as pd

# read the first excel file
df1 = pd.read_excel('full_music_data.xlsx') #是字符串
df1['ID'] = df1['ID'].apply(lambda x: int(x.split(',')[0]))

# read the second excel file
df2 = pd.read_excel('Blues.xlsx')
df2['ID'] = df2['ID'].astype(int)

merged_df = pd.merge(df1, df2, on='ID', how='left')

merged_df.to_excel('merged_data.xlsx', index=False)
'''

import pandas as pd

# read the first excel file
df1 = pd.read_excel('full_music_data.xlsx', dtype={'ID': str})


# read the second excel file
df2 = pd.read_excel('Blues.xlsx', dtype={'ID': str})

merged_df = df1[df1['ID'].str.contains('|'.join(df2['ID']))]
#merged_df = pd.merge(df1, df2, left_on='ID', right_on='ID', how='left', suffixes=('_left', '_right'))
merged_df.to_excel('merged_data.xlsx', index=False)

