

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
#%%
df['overweight'] = (df['weight'] / ((df['height']/ 100) ** 2) > 25).astype(int) 
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# %%
df_cat = df.melt(id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'smoke', 'alco', 'active', 'overweight'])


# Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
# df_cat = pd.DataFrame(df_cat.groupby(['cardio', 'variable',	'value']).size().reset_index(name = 'counts'))

# # Draw the catplot with 'sns.catplot()'
# graph = sns.catplot(
#     x='variable',
#     y='counts',
#     hue='value',
#     col='cardio',
#     data=df_cat,
#     kind='bar')
# %%
df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & 
            (df['height'] >= df['height'].quantile(0.025)) &
            (df['height'] <= df['height'].quantile(0.975))&
            (df['weight'] >= df['weight'].quantile(0.025)) &
            (df['weight'] <= df['weight'].quantile(0.975))]

# %%
corr = df_heat.corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.tril_indices_from(mask)] = True
# %%
# Draw the heatmap with 'sns.heatmap()'
sns.heatmap(corr, mask=mask)

# %%
