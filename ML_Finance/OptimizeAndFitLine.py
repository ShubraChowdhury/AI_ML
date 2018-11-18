# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:49:38 2016

@author: DevAdmin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

def error(line, data):
    """ Compute error between a given line model and observed data
    
    Parameters
    line : tuple/list/array (C0,C1) where C0 is the slope of the line 
    and C1 is the intercept of the line 
    data : 2D array where each row is a point (x,y)
    
    Return: error as a single real value 
    
    """
    """ If we sum up the squares of the residuals of all the points 
    from the line we get a measure of the
    fitness of the line. Our aim should be to minimize this value.
    equation is y =mx + c so the error or residual 
    so the residual = y - (mx=c) , sum of error = (y -(mx+c))^2
    data[:,1] = y value , data[:,0] = x value
    """
    err = np.sum((data[:,1] - (line[0]*data[:,0]+line[1]))**2)
    
    return err
def fit_line(data, error_func):
    """ Fit the line to a given data , using supplied error function
    Parameters
    data : 2D array where each row is a point (x0,y)
    error_func: function that computes the error between 
    a line and observed data 
    
    Returns: the line that minimizes the error function 
    """
    
    """ Generate initial guess for this model """
    l = np.float32([0,np.mean(data[:,1])])
    x_ends = np.float32([-5,5])
    plt.plot(x_ends,l[0]*x_ends + l[1],'m--',linewidth=2, label="Initial Guess")
    
    result = op.minimize(error_func,l,args=(data,),method='SLSQP',options={'disp':True})
    
    return result.x
    
def test_run():
    """ Define Original Line """
    l_orig = np.float32([4,2])
    print("Original Line: C0={}, C1={}".format(l_orig[0],l_orig[1]))
    Xorig = np.linspace(0,10,21)     
    Yorig = l_orig[0]*Xorig + l_orig[1]
    plt.plot(Xorig,Yorig,'b',linewidth=2, label ="Original Line")
    
    
    """ Introduce Noice """
    
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma,Yorig.shape )
    data = np.asarray([Xorig,Yorig+noise]).T
    plt.plot(data[:,0],data[:,1],'go',label="Data points")
    
    """ Try to fit the line to this data """
    l_fit = fit_line(data , error)
    print("Fitted Line: C0={}, C1={}".format(l_fit[0],l_fit[1]) )
    plt.plot(data[:,0],l_fit[0]*data[:,0]+l_fit[1],'r--',label="Fitted Line")
#  
    
if __name__ =="__main__":
    test_run()      
