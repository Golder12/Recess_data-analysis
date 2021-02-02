# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

import pandas as pd
df = pd.read_csv('UceResultsBySchool2011-2016.csv')
df

df.columns

# Cleaning up the white spaces in the column labels

df.columns = df.columns.map(str.strip)
df.columns

# # Number of schools in 20 top districts

year_grup = df.groupby(['YEAR'])
year_2016 = year_grup.get_group(2016)
show = year_2016['DISTRICT'].value_counts().head(20)
show

ax = show.plot(kind='bar', rot=20, figsize=(20,15), fontsize=15)
ax.set_title('DISTRICTS WITH THE MOST SCHOOLS', fontsize=20)
ax.set_xlabel('Districts', fontsize=20)
ax.set_ylabel('Number of schools', fontsize=20)


# # Determine best performing schools each year

# Creating a score column that aggregates the percentages of the different divisions, attaching different weights to each of them. The score ranges from 0 to 100

def score(x):
    return x['% DIV 1'] + x['% DIV 2']*0.5 + x['% DIV 3']/float(3) + x['% DIV 4']*0.25 + x['% DIV 7']*0.1 + x['% DIV 9']*0.1 + x['% X']*0.0
df['SCORE'] = df.apply(score, axis=1)

# Using the scores column to obtain best performing schools per year

year_grup = df.groupby('YEAR')

# Best performing schools added to df_ranks dictionary

df_ranks = {}
for YEAR, group in year_grup:
    df_ranks[YEAR] = group[['SCHOOL', 'SCORE']].sort_values(by='SCORE', ascending=False)

# Displaying top ten in each year

for YEAR in df_ranks:
    print(str(YEAR)+"'s 10 best schools:")
    print(df_ranks[YEAR][:10].reset_index().drop('index', axis=1))
    print('\n')

# # Number of students sitting in every district

df.columns = df.columns.map(str.strip)
ydt = df[['YEAR', 'DISTRICT', 'TOTAL CANDIDATES']]
y_d_t = ydt.groupby(['YEAR', 'DISTRICT'])['TOTAL CANDIDATES'].sum().reset_index().sort_values(by=['YEAR', 'TOTAL CANDIDATES'], ascending=[True, False])
y_d_t = y_d_t.reset_index().drop('index', axis=1)
y_d_t


