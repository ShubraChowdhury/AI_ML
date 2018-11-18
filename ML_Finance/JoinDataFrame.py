# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:27:49 2016

@author: DevAdmin
"""

import pandas as pd

infile = 'F:/Training/MachineLearningGeorgiaTech/01-02/'

def test_run():
    symbol ="SPY"
    """ Tell the CSV file that Index Column id Date and not the 
    auto generated sequence number"""
    dfSPY = pd.read_csv(infile+"{}.csv".format(symbol), index_col="Date", parse_dates=True, usecols=['Date','Adj Close'],  na_values=['nan'])
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date,end_date)
    df1 = pd.DataFrame(index = dates)
    #print(dfSPY)
    
    df1 = df1.join(dfSPY)
    """ Dropping NaN Values for SPY """
    df1=df1.dropna()
    print(df1)
    

if __name__ =="__main__" :
    test_run()