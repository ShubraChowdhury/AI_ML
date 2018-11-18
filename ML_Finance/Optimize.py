# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 07:41:04 2016

@author: DevAdmin
"""
import scipy.optimize as op
import numpy as np
import matplotlib.pyplot as plt
def f(X):
    Y = (X -1.5)**2 + 0.5
    
    print("X ={} , Y= {}".format(X,Y) )
    return Y
    
def test_run():
    Xguess =2
    
    min_result = op.minimize(f, Xguess, method='SLSQP', options={'disp':True})
    print("X={}, Y={}".format(min_result.x,min_result.fun))
    
    xplot = np.linspace(0.5,2.5,21)
    yplot = f(xplot)
    
    plt.plot(xplot,yplot)
    plt.plot(min_result.x,min_result.fun,'ro')
    plt.title("Minima of an Objective Function")
    plt.show()
    
if __name__ =="__main__":
    test_run()    