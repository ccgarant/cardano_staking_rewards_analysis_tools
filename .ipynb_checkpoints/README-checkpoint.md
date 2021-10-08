# Cardano Staking Analysis Tool for Daedalus Wallet Staking Rewards Exports
By: Christophe Garant


## Description
A script to read Daedalus staking rewards .csv files, clean, aggregate, and format data for easy rewards anaylsis, report, dataviz, and excel sheet.

![](pics/dataframes.png)

###  Problems solved:
- current individual .csv files for each epoch date are hard to perform analysis on.
    - files only give total rewards for given epoch date.
        - hard to see rewards received for current epoch.
        - hard to analyze results over timespans.
        - hard to perform any time of data analysis without manual labor to format and gather.
    - files can have inconsistent reward amount data types, e.g. float or string.  
        - When you reach the thousands for rewards (e.g. 1,234), the file returns the number with a comma into a string ("1,234").  Turns reward amounts into mixed data types cannot perform math on.
    - files can return different subset of wallets over time (e.g. if you added or renamed a wallet)
- no performance report or useful data visualization of rewards portfolio.


### Benefits:
- returns report of total rewards per wallet, and rewards per epoch, in ADA and USD price.
- returns `df` pandas dataframe of total rewards, index of dates, columns of wallets.
- returns `df_e2e` pandas dataframe of rewards epoch-to-epoch, index dates, columns wallets.
- exports `df` and `df_e2e` to excel sheet for more analysis (custom dataviz, etc).
- returns rewards analysis summary and dataviz charts in console (IPython best).


### How To Steps
1. Clone this github to folder on your local computer.  
     - Delete fake data in `~\data` folder.  This is for example only.  
     - Or, keep fake .csv if you want to test the script for example.
2. From Daedalus, start exporting your staking rewords .csv files every epoch to directory `~\data`
3. Open IPython terminal and change directory to staking analysis folder (base directory).
    - where `staking_analysis.py` lives, and make sure folder `~\data` has .csv files and `staking_file_cleanup_v2.py`.
4. Run `staking_analysis.py` by `%run staking_analysis` in base directory.
    * put in current ada price when prompted
5. Enjoy!
    - ![](pics/console.png)
    - ![](pics/console_zoom.png)
    - ![](pics/dataframes.png)


    
    
## TODO
- better dataviz, analysis, and jupyter notebook for reporting
- better fake dataset

Please comment or suggest improvements, hope you find this helpful.  Thanks!


