# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 09:03:40 2016

@author: DevAdmin
"""

import time 
import numpy as np

def test_run():
    t1 = time.time()
    
    print(t1)
    nd1 = np.random.random((1000,10000))
    print(" Do some stuff ", np.random.randint(0,10,size=(5,4)))
    
    t2 = time.time()
    
    print(t2)
    dif =(t2-t1)
    print("Execution Time =",dif)

if __name__ == "__main__":
    test_run()