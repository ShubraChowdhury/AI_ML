# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:59:26 2016

@author: DevAdmin
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

infile = 'C:/Training/udacity/MachineLearningGeorgiaTech/data/'

def get_dir_path(symbol,basedir =infile):
    return os.path.join(basedir+"{}.csv".format(str(symbol)))
    

def get_data(symbols, dates):
    df = pd.DataFrame(index=dates)
#    if 'SPY' not in symbols:    
#        symbols.insert(0,'SPY')
    
    for symbol in symbols:
       df_ticker=pd.read_csv(get_dir_path(symbol), index_col='Date', 
                             parse_dates=True, usecols=['Date','Adj Close'],
                             na_values=['nan'])
       df_ticker = df_ticker.rename(columns={'Adj Close':symbol})
       df = df.join(df_ticker)
# The how =inner causes the graph to reverse rather use dropna##
#       df = df.join(df_ticker,how ="inner")
       
       if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])
       
    return df
    
#def normalize_data(df):
#    return df/df.ix[0,:]
    
def plot_data(df, title='STOCK '):
#    df = normalize_data(df)
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()
    

def test_run():
        dates = pd.date_range('2010-01-01', '2010-12-31')
        
        symbols =['SPY','IBM']
        
        df = get_data(symbols, dates)
        ax = df['SPY'].plot(title="SPY Rolling Mean", label ="SPY")
        rolling_mean = pd.rolling_mean(df['SPY'],window =20)
        rolling_mean.plot(label="Rolling Mean SPY", ax =ax)
        
        
        df['IBM'].plot( label ="IBM")
        rolling_mean1 = pd.rolling_mean(df['IBM'],window =20)
        rolling_mean1.plot(label="Rolling Mean IBM", ax =ax)
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend(loc="upper right")
        
        print('\n Median \n',df.median())
        print('\n SD \n',df.std())
        plt.show()

    
if __name__ == "__main__":
    test_run()