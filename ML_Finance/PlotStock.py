# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:43:50 2016

@author: DevAdmin
"""
import pandas as pd
import matplotlib.pyplot as pl

infile = 'C:/Training/udacity/MachineLearningGeorgiaTech/data/'


def test_run():
    symbol ="APPL"
    df = pd.read_csv(infile+"{}.csv".format(symbol))
    #print(df.tail())
    print('Adj Close')
    df['Adj Close'].plot()
    pl.show()
    
    return df['Volume'].mean()
    
        
if __name__ == "__main__":
    xx=test_run()
    print("Volume Mean ",xx)
