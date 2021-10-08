#!/usr/bin/env python
# coding: utf-8

# # Cardano Staking Analysis for Daedalus Wallet Staking Rewards Exports
# By: Christophe Garant

#import
import pandas as pd
import matplotlib.pyplot as plt
from os import listdir, chdir, getcwd

#get base current folder working directory
base = getcwd()

#change directory to data folder where data and staking_file_cleanup_v2 exists
chdir('data')

#import and clean data, bring in 
# df - dataframe of total rewards, index dates, columns wallets 
# df_e2e - dataframe of rewards epoch-to-epoch, index dates, columns wallets 
from staking_file_cleanup_v2 import df, df_e2e

#come back to working directory base folder
chdir(base)

# get current price of Ada for analysis
current_ada_price = input('\n\n\What is the current Ada price?:\n\n')
current_ada_price = float(current_ada_price)

# Analysis

## Report Summary
print(f'\nStaking Rewards Report *THIS EPOCH* (USD)')
print(f'\n{round(df_e2e.iloc[-1].sum()*current_ada_price,1)} Total Rewards Received!')
print(f'{round(df_e2e.iloc[-5:].mean().sum()*current_ada_price,1)} Total Rewards Received Mean Last 5 Epochs!')
print(f'{round(df_e2e.mean().sum()*current_ada_price,1)} Total Rewards Received All Time {len(df_e2e)} Epochs!')

print(f'\nStaking Rewards Report *THIS EPOCH* (ADA)')
print(f'\n{round(df_e2e.iloc[-1].sum(),1)} Total Rewards Received!')
print(f'{round(df_e2e.iloc[-5:].mean().sum(),1)} Total Rewards Received Mean Last 5 Epochs!')
print(f'{round(df_e2e.mean().sum(),1)} Total Rewards Received All Time {len(df_e2e)} Epochs!')


#plot function vertical bar charts
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
    df.plot(kind='bar',stacked='True',title=title,figsize=(12,6))
    plt.xticks(rotation=45, ha='right')
    plt.show()


## Plots
plotStaking(df,'Staking Rewards Total Per Wallet ADA')
plotStaking(df*current_ada_price,'Staking Rewards Total Per Wallet USD')
plotStaking(df_e2e,'Staking Rewards Per Epoch Per Wallet ADA')
plotStaking(df_e2e*current_ada_price,'Staking Rewards Per Epoch Per Wallet USD')



## Report Details
print(f'\nRewards Received Per Wallet (ADA)\n\n{round(df_e2e.iloc[-1],1)}\n')
print(f'\nMean Rewards Received Per Wallet Last 5 Epochs (ADA)\n\n{round(df_e2e.iloc[-5:].mean(),1)}\n')
print(f'\nMean Rewards Received Per Wallet All Time Epochs (ADA)\n\n{round(df_e2e.mean(),1)}\n')

print(f'\nDescription: Last 5 epochs (25 days) (ADA)\n\n{df_e2e.iloc[-5:].describe()}\n')
print(f'\nDescription: All time {len(df_e2e)} epochs (ADA)\n\n{df_e2e.describe()}\n')

print('\nStaking Report in ADA\n')
print(f'\nStaking Total Summary (ADA):\n\n{df}\n')
print(f'\nStaking Epoch 2 Epoch Summary (ADA):\n\n{df_e2e}\n')

print('\nStaking Report in USD\n')
print(f'\nStaking Total Summary (USD)\n\n{df*current_ada_price}\n')
print(f'\nStake Results Per Epoch (Stake2Stake) (USD)\n\n{df_e2e*current_ada_price}\n')




## Export
with pd.ExcelWriter('staking_analysis.xlsx') as writer:  
    df.to_excel(writer, sheet_name='total')
    df_e2e.to_excel(writer, sheet_name='per_epoch')
