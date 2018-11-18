# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

infile = 'C:/Training/udacity/MachineLearningGeorgiaTech/data/APPL.csv'

def test_run(infile):
    df = pd.read_csv(infile)
#    print (df)
#    
#    print (df.tail())
#    print (df.head())
    print('Rows between 10 and 15')
    print(df[10:16])
    
if __name__ == "__main__":
    test_run(infile)