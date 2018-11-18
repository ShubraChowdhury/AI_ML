# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 10:18:25 2016

@author: DevAdmin
"""


import numpy as np
from time import time

def how_long(func,*args):
    t0 = time()
    result = func(*args)
    t1 = time()
    return result, t1-t0

def manual_mean(arr):
    sum =0
    for i in range(0,arr.shape[0]):
        for j in range(0,arr.shape[1]):
            sum = sum+arr[i,j]
    return sum/arr.size
    

def numpy_mean(arr):
    return arr.mean()
    

def test_run():
  
   nd1 = np.random.random((1000,10000))
   
   """ Time 2 functions """
   
   res_manual, t_manual = how_long(manual_mean,nd1)
   res_numpy, t_numpy = how_long(numpy_mean,nd1)
   
   #print (res_manual, t_manual,res_numpy, t_numpy)
   
   assert abs(res_manual - res_numpy )   <= 10e-6

   speedup =  t_manual/ t_numpy

   print("\n Manual: {:.6f} ({:.3f} secs.) vs Numpy: {:.6f} ({:.3f} secs.)".format(res_manual, t_manual,res_numpy, t_numpy) )  

   print ("\n Numpy is ,",speedup," times faster than manual loop" )  
   
if __name__ == "__main__":
    test_run()