#!/usr/bin/env python
# coding: utf-8

"""
# Cardano Daedalus Staking Rewards Cleaning and Aggregation to Prep for Analysis
By: Christophe Garant, 1/21/21

This file cleans and aggregates the daedalus rewards .csv files 
to be ready for data analysis.

Returns:
- df - the dataframe of total wallet rewards, wallets as columns, date of issuance as index
- df_e2e - the dataframe of epoch-to-epoch wallet rewards, i.e. the rewards for that epoch of date received, wallets as columns, date of issuance as index


### Updates
* 1/21/21 - initial release
* 10/8/21 - total revamp. updated to crunch numbers on daedalus updated rewards .csv format, some cleaning of code

"""

# imports
import pandas as pd
from os import listdir, chdir, getcwd
from pprint import pprint
from numpy import zeros as np_zeros


#get the listed directory and save as list
list_dir = listdir()

# create sorted list of daedalus exported staking reward .csv staking reward files
list_rewards = [x for x in list_dir if (('Rewards' in x) & ('.csv' in x))]
list_rewards = sorted(list_rewards)
# print('\nReward Files Found:\n')
# pprint(list_rewards)

# grab all wallet names from all staking rewards
# there may be scenarios where you create a new wallet, and prior rewards
# do not have the new wallet.  This will create a list of all unique wallets
wallets_all = []
for reward in list_rewards:
    wallet_list = pd.read_csv(reward)['Wallet'].to_list()
    for wallet in wallet_list:
        if wallet in wallets_all:
            pass
        else:
            wallets_all.append(wallet)

            
#sort wallets in order
wallets_all = sorted(wallets_all)
# print(f'\nTotal wallets found: {wallets_all}\n')


def cleanAdaRewardsCSVForDF(csv_file):
    df = pd.read_csv(csv_file,usecols=[0,2,3],index_col=[0])
    if df['Total rewards earned (ADA)'].dtype == 'O':
        df['Total rewards earned (ADA)'] = df['Total rewards earned (ADA)'].str.replace(',','')
    df['Total rewards earned (ADA)'] = pd.to_numeric(df['Total rewards earned (ADA)'])
    df['Date'] = pd.to_datetime(df['Date'])
    wallets_local = df.index.to_list()
    date = df['Date'][0].date()
    reward = df['Total rewards earned (ADA)'].to_list()
    return df, wallets_local, date, reward


wallets= []
rewards = []
dates = []
dict_reward_holder = {}

#create empty temp holding dictionary of all wallets for looping thru wallets and rewards per csv
for wallet in wallets_all:
    dict_reward_holder[wallet]=0
# print(dict_reward_holder)

#create dataframe for all rewards
dfr = pd.DataFrame(index=wallets_all)

# print(dict_reward_holder)

#loop thru the list of .csv files, and within each .csv file,
#populate the temp holding empty dictionary of wallets and rewards,
#read in wallets and rewards in the dfr rewards dataframe, new columns for each date, wallets as index
for file in list_rewards:
#     print(file)
    [df,wallets_local,date,reward] = cleanAdaRewardsCSVForDF(file)
    wallets.append(wallets_local)
    rewards.append(reward)
    dates.append(date)
    for i in range(len(wallets_local)):
    #     print(wallets_local[i])
    #     print(reward[i])
        key = wallets_local[i]
        value = reward[i]
    #     print(key,value)
        dict_reward_holder[key]=value
    dfr[str(date)] = dict_reward_holder.values()

#transpose columns and index (e.g. switch) so that dates are the index and columns are the wallets,
#the easiest way I could think of to read in the format for each .csv into dataframe...
dfr = dfr.transpose()
dfr.index = pd.to_datetime(dfr.index) #typecast index from string to datetype format 
dfr.index.name = 'date'               #name new index
df = dfr.copy()

## uncomment to print these if needed for understanding
# print(wallets)
# print(dates)
# print(rewards)
# print(dfr)

#dataframe from epoch-to-epoch differences, e.g. the rewards received for that epoch,
#daedalus reward files gives you the total rewards per wallet, but this is not handy,
#for understanding staking rewards per epoch (73 in 1 year, or every 5 days.)
df_e2e = df.diff()[1:]

## print if needed
# print(df)
# print(df_e2e)