#!/usr/bin/env python
# coding: utf-8

# # Cardano Staking Total Ada Calc
# By: Christophe Garant

#import
import pandas as pd
import numpy as np

current_ada_price = input('\n\n\What is the current Ada price?:\n\n')
current_ada_price = np.float(current_ada_price)

#read in cleaned staking data from daedalus csv files (see prior cleaning script)
df = pd.read_excel('staking_master.xlsx',sheet_name='total')
df = df.set_index('date')                #set index to date
df.index = pd.to_datetime(df.index)      #set index to datetime

df_s2s = pd.read_excel('staking_master.xlsx',sheet_name='per_epoch')
df_s2s = df_s2s.set_index('date')                #set index to date
df_s2s.index = pd.to_datetime(df_s2s.index)      #set index to datetime


df_wallet = pd.DataFrame(index=['date'],columns=['CCG5','CCG4','CCG3','CCG2','CCG'])

### 2021-02-15
df_wallet.loc['2021-02-15'] = [
    23_323.114372,
    19_391.647028,
    19_400.074428,
    19_391.647028,
    19_531.051472
    ]

total_ada = df_wallet.loc['2021-02-15'].sum()

print('')
print(f'Total Ada: {round(total_ada,2)}')
print(f'Total USD: {round(total_ada*current_ada_price,2)}')

