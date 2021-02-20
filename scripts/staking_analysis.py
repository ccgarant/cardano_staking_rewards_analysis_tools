#!/usr/bin/env python
# coding: utf-8

# # Cardano Staking Analysis for Daedalus Wallet Staking Rewards Exports
# By: Christophe Garant

#import
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from os import listdir, chdir, getcwd

# get current price of Ada for analysis
current_ada_price = input('\n\n\What is the current Ada price?:\n\n')
current_ada_price = np.float(current_ada_price)


#change directory to data files
chdir('..')
chdir('data')
#read in cleaned staking data from daedalus csv files (see prior cleaning script)
df = pd.read_excel('staking_master.xlsx',index_col='date')
#df.index = df.index.strftime('%Y-%m-%d')
#df = df.set_index('date')                #set index to date
df.index = pd.to_datetime(df.index)      #set index to datetime



print('')
print(f'\nStaking Total Summary:\n\n{df}')
print('')

#create stake to stake epoch results by taking the row difference
df_s2s = df.diff()
df_s2s = df_s2s[1:]  #first row is NaN given non existent difference to start


## analysis

#best performing stake pool (sp) this epoch
sp_best_performer_this_epoch = df_s2s.iloc[len(df_s2s)-1].sort_values(ascending=False)

#rewards total this epoch
rewards_total_this_epoch = df_s2s.iloc[len(df_s2s)-1].sum()

#rewards total mean
sp_best_performer_mean = df_s2s.mean()
sp_best_performer_mean = sp_best_performer_mean.sort_values(ascending=False)

#rewards total this epoch
rewards_total = df.iloc[len(df)-1].sum()


## Report

print('\nStaking Report in Ada\n')
print(f'\nStake Results Per Epoch (Stake2Stake)\n\n{df_s2s}\n')
print(f'\nBest Performing Stake Pool This Epoch:\n\n{sp_best_performer_this_epoch}\n')
print(f'\nBest Performing Stake Pool Mean:\n\n{sp_best_performer_mean}\n')
print(f'\nStaking Rewards Total this Epoch:\n\n{round(rewards_total_this_epoch,2)}\n')
print(f'\nStaking Rewards Total:\n\n{round(rewards_total,2)}\n')

print('\nStaking Report in USD\n')
print(f'\nStake Results Per Epoch (Stake2Stake)\n\n{df_s2s*current_ada_price}\n')
print(f'\nBest Performing Stake Pool This Epoch:\n\n{sp_best_performer_this_epoch*current_ada_price}\n')
print(f'\nBest Performing Stake Pool Mean:\n\n{sp_best_performer_mean*current_ada_price}\n')
print(f'\nStaking Rewards Total this Epoch:\n\n${round(rewards_total_this_epoch*current_ada_price,2)}\n')
print(f'\nStaking Rewards Total:\n\n${round(rewards_total*current_ada_price,2)}\n')


## Plots

def plotStaking(df,title):
    '''
    plots stacking results per epoch, in a stack bar plot
    
    input:
        df - dataframe of staking results per epoch (stake-2-stake)
        title - plot title
    output:
        plot
        
    '''   
    
    # Initialize the matplotlib figure
    #f, ax = plt.subplots(figsize=(12, 6))
    df.plot(kind='bar',stacked='True',title=title)
    plt.xticks(rotation=45, ha='right')
    plt.show()



plotStaking(df_s2s,'Staking Rewards Per Epoch Per Wallet ADA')
plotStaking(df,'Staking Rewards Total Per Wallet ADA')

plotStaking(df_s2s*current_ada_price,'Staking Rewards Per Epoch Per Wallet USD')
plotStaking(df*current_ada_price,'Staking Rewards Total Per Wallet USD')


## Export

with pd.ExcelWriter('staking_master.xlsx') as writer:  
    df.to_excel(writer, sheet_name='total')
    df_s2s.to_excel(writer, sheet_name='per_epoch')

chdir('..')
chdir('scripts')
