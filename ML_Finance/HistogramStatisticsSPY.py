# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 12:43:27 2016

@author: DevAdmin
"""

import os
import pandas as pd

import  matplotlib.pyplot as plt

infile = 'F:/Training/MachineLearningGeorgiaTech/data/'

def symbol_to_path(symbol, base_dir=infile):
    """Return CSV file path given ticker symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':  # drop dates SPY did not trade
            df = df.dropna(subset=["SPY"])

    return df


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

def compute_daily_returns(df):
    """Compute and return the daily return values."""
    # TODO: Your code here
    # Note: Returned DataFrame must have the same number of rows
    daily_return = df.copy()
    daily_return[1:] = (df[1:]/df[:-1].values)-1
    daily_return.ix[0,:] =0 
    return daily_return
    
    
def test_run():
    dates = pd.date_range('2009-01-01', '2012-12-31')
    symbols =['SPY','XOM']
    df = get_data(symbols,dates)
    plot_data(df)

    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")
    
    #daily_returns['SPY'].hist()
    daily_returns['SPY'].hist(bins=20)
    
    meanspy = daily_returns['SPY'].mean()
    std = daily_returns['SPY'].std()
    #print(meanspy, std)
    
    plt.axvline(meanspy, color='w', linestyle='dashed', linewidth=2)
    plt.axvline(std, color='r', linestyle='dashed', linewidth=2, label='SD')
    plt.axvline(-std, color='r', linestyle='dashed', linewidth=2, label='SD')

    print('\n',daily_returns['SPY'].kurtosis())
    
    daily_returns.hist(bins=20)
    daily_returns['SPY'].hist(bins=20,label='SPY')
    daily_returns['XOM'].hist(bins=20,label='XOM')
    plt.legend(loc = 'upper right')
    
if __name__ =="__main__":
    test_run()