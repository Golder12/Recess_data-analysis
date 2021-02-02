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

r = pd.read_csv('UceResultsBySchool2011-2016.csv')
r

pd.set_option('display.max_columns',48)

r



r.loc[1, 'MALE TOTAL X '] = 1
r 

r.fillna(0, inplace = True)
r

d = pd.read_csv('UceResultsBySchool2011-2016.csv')
d


