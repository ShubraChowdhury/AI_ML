# -*- coding: utf-8 -*-
"""
Created on Mon May  2 07:38:23 2016

@author: DevAdmin
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 08:49:38 2016

@author: DevAdmin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

def error_poly(C, data):
    """ Compute error between a given Polynomial model and observed data
    
    Parameters
    C: numpy.poly1d object or equivalent array representing polynomial coefficient
    data : 2D array where each row is a point (x,y)
    
    Return: error as a single real value 
    
    """
    """ 
    Metric: Sum of squared Y-axis differences
    """
    err = np.sum((data[:,1] - np.polyval(C,data[:,0]))**2)
    
    return err
    
def fit_poly(data, error_func, degree=3):
    """ Fit the Polynomial to a given data , using supplied error function
   
    Parameters
    data : 2D array where each row is a point (x0,y)
    error_func: function that computes the error between 
    a polynomial and observed data 
    
    Returns: the polynomial that minimizes the error function 
    """
    
    """ Generate initial guess for polynomial  model (all coeffs =1)"""
    Cguess =np.poly1d(np.ones(degree+1,dtype=np.float32))
    #l = np.float32([0,np.mean(data[:,1])])
    x = np.linspace(-5,5,21)
#    print(x)
    plt.plot(x,np.polyval(Cguess,x),'m--',linewidth=2, label="Initial Guess")
    
    result = op.minimize(error_func,Cguess,args=(data,),method='SLSQP',options={'disp':True})
    
    return  np.poly1d(result.x)
    
def test_run():
    """ Define Original Line """
    #l_orig = np.float32([4,2])
    
    Xorig = np.linspace(-10,50,21)     
    Yorig =  1.5*(np.power(Xorig,4)) - 10 *(np.power(Xorig,3)) + 60*Xorig  +50
    print("Original Line: X={}, Y={}".format(Xorig,Yorig))    
    plt.plot(Xorig,Yorig,'b',linewidth=2, label ="Original Line")
    
    
    """ Introduce Noice """
    
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma,Yorig.shape )
    data = np.asarray([Xorig,Yorig+noise]).T
#    print(data[:,0])
    plt.plot(data[:,0],data[:,1],'go',label="Data points")
   # x = np.linspace()
    #print(x)   
    """ Try to fit the Ploy to this data """
    l_fit = fit_poly(data , error_poly,3)
    print('data 0:-',data[:,0],'\n data 1:',data[:,1])
    print('data:-',l_fit[0], '---',l_fit[1],'---',l_fit[2],'--',l_fit[3],'\n',l_fit)
    #Yfitted = 
#    print("Fitted Line: Xnew={}, Ynew={}".format(l_fit[0],l_fit[1]) )
    plt.plot(data[:,0],data[:,1],'r--',label="Fitted Line")
#  
    
if __name__ =="__main__":
    test_run()      
