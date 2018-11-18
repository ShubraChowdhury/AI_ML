# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 08:55:40 2016

@author: DevAdmin
"""

"""Compute daily returns."""

import os
import pandas as pd
import matplotlib.pyplot as plt

infile = 'C:/Training/udacity/MachineLearningGeorgiaTech/data/'

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
#    print(df)
#    print(df[1:])
#    print(df[:-1])
#    print((df[1:]/df[:-1].values))
    daily_return[1:] = (df[1:]/df[:-1].values)-1
    daily_return.ix[0,:] =0 
#    print(daily_return)
    return daily_return

def compute_cumm_returns(df):
    """Compute and return the daily return values."""
    # TODO: Your code here
    # Note: Returned DataFrame must have the same number of rows
    df1 = df.copy()
    cumm_return = df.copy()
    
    """ Assign the first row of the data frame to all the rows 
    so that we can calculate the df[1:]/df[0:1]
    """
    df1.iloc[0:,0:]=cumm_return[0:1].values
#    print(cumm_return[0:].values)
#    
#    print(df1)
#    print(df)
#    print(df[0:1].values)
#    df1[:]=df[0:1].values
#    print('First Row \n',df1)
#    print('All Row after First Row \n',df[1:])
#    print('Division \n',df[:-1]/df1)
##    print((df[1:]/df[:-1].values))
    cumm_return[1:] = (df[1:]/df1)-1
    cumm_return.ix[0,:] =0 
#    print(cumm_return)
    return cumm_return

def test_run():
    # Read data
    dates = pd.date_range('2012-07-01', '2012-07-10')  # one month only
    symbols = ['SPY','XOM']
    df = get_data(symbols, dates)
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")
    
    cumm_return= compute_cumm_returns(df)
    plot_data(cumm_return, title="Cummulative returns", ylabel="Cummulative returns")
if __name__ == "__main__":
    test_run()