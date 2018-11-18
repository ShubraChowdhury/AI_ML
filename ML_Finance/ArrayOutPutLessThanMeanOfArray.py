# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:02:25 2016

@author: DevAdmin
"""
import numpy as np

def test_run():
    
    a = np.array([(20,30,40,50,10,0),(11,21,31,0,41,51)])
    
    mean = a.mean()
    print('\n',a)
    print('\n',mean)
    print('\n', a[a <mean])
    
    
if __name__ == "__main__":
    test_run()
