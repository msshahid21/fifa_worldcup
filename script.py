# Importing required data-analysis libraries
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# Importing World Cup Dataset
df = pd.read_csv('WorldCupMatches.csv')

# Creating new column in df for total goals
df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']

# Barplot for total goals scored each world cup tournament between 1930 - 2014
sns.set_style('whitegrid')
sns.set_context('notebook', font_scale=1.25)
f, ax = plt.subplots(figsize=(14, 7))
ax = sns.barplot(
    data = df,
    x = 'Year',
    y = 'Total Goals')
ax.set_title('Average Goals Scored Each Year')
plt.show()

# Importing Goals Dataset
df_goals = pd.read_csv('goals.csv')

# Creating Boxplot for goals dataset
f, ax2 = plt.subplots(figsize=(14, 7))
ax2 = sns.boxplot(
    data = df_goals,
    x = 'year',
    y = 'goals',
    palette = ('Spectral'))
ax2.set_title('Goals Scored Per Game Each Year')
plt.show()