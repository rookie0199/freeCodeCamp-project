#%%
import matplotlib.pyplot as plt
import pandas as pd
from pandas.io import parsers
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
import numpy as np
#%%
# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col=['date'])


#%%
# Copy and modify data for monthly bar plot
df_bar = df.copy()
df_bar['year'] = df_bar.index.year
df_bar['month'] = df_bar.index.strftime('%B')
months = ["January", 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
df_bar['month'] = pd.Categorical(df_bar['month'], categories=months, ordered=True)
df_bar = df_bar.sort_values(by='month')

df_bar = pd.pivot_table(df_bar, values="value", index="year", columns="month", aggfunc = np.mean)
#%%
# Draw bar plot
ax = df_bar.plot(kind='bar')
ax.legend()
ax.set_xlabel("Years")
ax.set_ylabel("Average Page Views")
fig = ax.get_figure()
# Save image and return fig (don't change this part)
fig.savefig('bar_plot.png')
# %%
