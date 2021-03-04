import pandas as pd


df = pd.read_csv('adult.data.csv')
min_work_hours = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = len(df.loc[df['hours-per-week'] == min_work_hours, 'age'])
rich_percentage = len(df.loc[(df['hours-per-week'] == min_work_hours) \
& (df['salary'] == '>50K'), 'age'])

print(rich_percentage)