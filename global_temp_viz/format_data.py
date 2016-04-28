__author__ = 'nerdless'

import pandas as pd

data_path = 'data/'
columns = range(13)
# Read the data in the data folder
global_df = pd.read_csv(data_path + 'GLB.Ts+dSST.csv', usecols=columns, na_values='**** ', index_col=0)
north_df = pd.read_csv(data_path + 'NH.Ts+dSST.csv', usecols=columns, na_values='**** ', index_col=0)
south_df = pd.read_csv(data_path + 'SH.Ts+dSST.csv', usecols=columns, na_values='**** ', index_col=0)

# This dict is used to rename the columns
months_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
               'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
               'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

# Renaming columns
global_df.rename(columns=months_dict, inplace=True)
north_df.rename(columns=months_dict, inplace=True)
south_df.rename(columns=months_dict, inplace=True)

# Create a new dataframe to store the formated data
formated = pd.DataFrame()
for year in global_df.index.tolist():
    for month in global_df.columns.tolist():
        formated.loc[str(year) + month, 'global'] = global_df.loc[year, month]
        formated.loc[str(year) + month, 'north'] = north_df.loc[year, month]
        formated.loc[str(year) + month, 'south'] = south_df.loc[year, month]

formated.dropna(how='all', inplace=True)
formated.to_csv(data_path + 'formated.csv', index_label='date')  # Save as csv




