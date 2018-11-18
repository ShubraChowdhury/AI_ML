# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 11:27:49 2016

@author: DevAdmin
"""

import pandas as pd

infile = 'F:/Training/MachineLearningGeorgiaTech/01-01/'

def test_run():
    #symbol ="SPY"
    #df = pd.read_csv(infile+"{}.csv".format(symbol))
    start_date = '2010-01-22'
    end_date = '2010-01-26'
    dates = pd.date_range(start_date,end_date)
    print(dates)
    print(dates[0])

if __name__ =="__main__" :
    test_run()