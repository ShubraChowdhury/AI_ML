# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:32:03 2016

@author: DevAdmin
"""
import pandas as pd

infile = 'C:/Training/udacity/MachineLearningGeorgiaTech/data/'

#infile = 'E:/udacity/MachineLearningGeorgiaTech/01-01/'

def get_max_close(symbol):
    
    df = pd.read_csv(infile+"{}.csv".format(symbol))
    return df['Close'].max()
    

def test_run():
    
    symbols =['APPL','IBM']
    
    for symbol in symbols:
        print ("Max Close")        
        print(symbol,get_max_close(symbol))
        
if __name__ =="__main__":
  test_run()     