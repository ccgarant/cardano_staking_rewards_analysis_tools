# cardano_staking_rewards_analysis_tools
 Scripts for analyzing Cardano staking rewards from Daedalus exported csv staking files.

Until the Cardano Node Wallet Daedalus staking reward analysis improves, here are helpful scripts to help you understand your staking rewards. 

## Highlights:
* clean total staking rewards per wallet, in pandas dataframe format (df)
* cleaned epoch staking rewards per wallet (stake-to-stake), in pandas dataframe format (df_s2s)
    * currently Daedalus just provides total rewards per wallet, not rewards for **this epoch** per wallet
* creates a cleaned excel file of staking reward totals per wallet

## How To Steps
1. From Daedalus, export staking rewords as .csv files every epoch to directory `data`
    * sample test staking reward data provided for example only
2. Go to directory `scripts`
3. Open IPython terminal 
4. Run `staking_file_cleanup.py` from `script` cwd by `%run staking_file_cleanup`
5. Run `staking_analysis.py` by `%run staking_analysis`
    * put in current ada price for updated USD analysis
    
See jupyter notebook below for examples. (**in work**)

Please comment or suggest improvements, hope you find this helpful.  Thanks.


