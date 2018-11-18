# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:07:18 2016

@author: DevAdmin
"""

import numpy as np

def test_run():
    np.random.seed(693)
    a = np.random.randint(0,10, size=5)  

#    a = np.random.rand(5)
    
    indices = np.array([1,1,2,3])
    
    print(a)
    print('\n',a[indices])
    

if __name__ == "__main__":
   test_run()