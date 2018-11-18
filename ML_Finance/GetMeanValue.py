# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:43:50 2016

@author: DevAdmin
"""
import pandas as pd

infile = 'C:/Training/udacity/MachineLearningGeorgiaTech/data/'

def get_mean_value(symbol):
    
    df = pd.read_csv(infile+"{}.csv".format(symbol))
    return df['Close'].mean()
    
def get_max_close(symbol):
    
    df = pd.read_csv(infile+"{}.csv".format(symbol))
    return df['Close'].max()
    
def get_std_close(symbol):
    
    df = pd.read_csv(infile+"{}.csv".format(symbol))
    return df['Close'].std()
        
def test_run ():
    
    symbols =['APPL','IBM']
    
    for symbol in symbols:
        
        print("\n Mean of Close Value")
        print(symbol , get_mean_value(symbol))
        
        print("\n Max of Close Value")
        print(symbol , get_max_close(symbol))
        
        print("\nSTD of Close Value")
        print(symbol , get_std_close(symbol))
        
if __name__ == "__main__":
    test_run()
