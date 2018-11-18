# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:27:49 2016

@author: DevAdmin
"""

import pandas as pd

infile = 'C:/Training/udacity/MachineLearningGeorgiaTech/data/'

#C:\Training\udacity\MachineLearningGeorgiaTech\data

def test_run():
    symbol ="SPY"
    """ Tell the CSV file that Index Column id Date and not the 
    auto generated sequence number"""
    dfSPY = pd.read_csv(infile+"{}.csv".format(symbol), index_col="Date", parse_dates=True, usecols=['Date','Adj Close'],  na_values=['nan'])
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})    
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date,end_date)
    df1 = pd.DataFrame(index = dates)
    #print(dfSPY)
    """ Dropping NaN Values for SPY  using how =inner """
   
    df1 = df1.join(dfSPY,how='inner')
    #df1=df1.dropna()
    
    symbols=['GOOG','IBM','GLD']
    
    for ticker in symbols:
        df_ticker = pd.read_csv(infile+"{}.csv".format(ticker),index_col="Date",parse_dates=True,usecols=['Date','Adj Close'],na_values=['nan'])
        df_ticker = df_ticker.rename(columns={'Adj Close':ticker})   
        df1 = df1.join(df_ticker)
    print(df1)
    

if __name__ =="__main__" :
    test_run()