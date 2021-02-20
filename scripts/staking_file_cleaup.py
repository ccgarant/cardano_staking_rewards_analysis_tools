#!/usr/bin/env python
# coding: utf-8

# # Cardano Staking Clean Up and Concat Script for Daedalus Wallet Staking Rewards Exports
# By: Christophe Garant

#imports
import pandas as pd
from os import listdir, chdir, getcwd
from pprint import pprint

#get the listed directory and save as list
chdir('..')
chdir('data')
list_dir = listdir()

# grab only the exported staking reward files from Daedalus, and create list list_rewards of such files
list_rewards = [x for x in list_dir if 'Rewards' in x]
print('\nReward Files Found:\n')
pprint(list_rewards)


# grab all wallet names from all staking rewards
# there may be scenarios where you create a new wallet, and prior rewards
# do not have the new wallet.  This will create a list of all unique wallets
wallets = []
for reward in list_rewards:
    wallet_list = pd.read_csv(reward)['Wallet'].to_list()
    for wallet in wallet_list:
        if wallet in wallets:
            pass
        else:
            wallets.append(wallet)
print(f'\nTotal wallets found:\n')
pprint(wallets)


# reads the date column in each csv file, and appends each date to list dates
dates = []
for reward_file in list_rewards:
    df2 = pd.read_csv(reward_file)['Date']
    date = pd.to_datetime(df2[1]).date()
    dates.append(date)

# from each file, read the rewards data, typecast as float,
# and append it to list rewards_data
rewards_data = []
master_list = []
for i in range(len(list_rewards)):
#    print(i)
    temp = pd.read_csv(list_rewards[i])
#    print(temp)
    rewards_temp = temp['Reward'].to_list()
    wallets_temp = temp['Wallet'].to_list()
#    print('\n',wallets,rewards,'\n')
    reward_num = []
    for x in rewards_temp:
        reward_num_raw=x.split(" ADA")[0]
        reward_num.append(reward_num_raw)
#    print(reward_num)
    z = zip(wallets_temp,reward_num)  #zipped
    d = dict(z)                  #dictionary
#    print(d)
    for wallet in wallets:
#        print(wallet)
        if wallet in d.keys():
            pass
        else:
            d[wallet] = 0  #if the wallet doesnt exist, create key and set to zero
#    print(d)
    master_list.append(d)


# create dataframe from list of dictionaries master_list, and dates.
# they are in the same order.
df = pd.DataFrame(index=dates,data=master_list)
df = df.astype(float)
df.index = pd.to_datetime(df.index)
df = df.sort_index()  # sort dates in descending order
df.index.name = 'date'  #name index
#print(df)


print('\nFinal Product "df":\n')
print(f'\n {df} \n')
print('\nScript Complete\n')

# export cleaned up df to excel
df.to_excel('staking_master.xlsx')
print('\n"df" cleanup staking exported to staking_master.xlsx\n')

# change back to script directory
chdir('..')
chdir('scripts')





