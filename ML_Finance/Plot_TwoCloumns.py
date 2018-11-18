# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:43:50 2016

@author: DevAdmin
"""
import pandas as pd
import matplotlib.pyplot as plt

infile = 'C:/Training/udacity/MachineLearningGeorgiaTech/data/'


def test_run():
    symbol ="WTI"
    df = pd.read_csv(infile+"{}.csv".format(symbol))
    print(df.tail())
    #print('High value')
    df[['Adj Close']].plot()
    plt.show()  
    print(df.dtypes)

if __name__ == "__main__":
    test_run()
    
    
