import pandas as pd

df = pd.read_csv('adult.data.csv')

race_count = df.loc[:,'race'].count()
print(race_count)
average_age_men = df.loc[df['sex'] == 'Male', 'sex'].mean()
print(average_age_men)
