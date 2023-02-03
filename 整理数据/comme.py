#将data_by_artist和NUM_GENRE合并起来

import pandas as pd

# read the first excel file
df1 = pd.read_excel('data_by_artist.xlsx')

# read the second excel file
df2 = pd.read_excel('NUM_GENRE.xlsx')

merged_df = df1.merge(df2, on='ID', how='left')

merged_df.to_excel('merged_data.xlsx', index=False)

