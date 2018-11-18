# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:39:38 2016

@author: DevAdmin
"""

import numpy as np

def test_run():
    
    print("Random seed initializing the pseudo-random number generator.\n",
          "Each time you run the random variable generator you will \n",
          "get the same value untill session is closed")
    np.random.seed(693)
    
    a = np.random.randint(0,10, size=(5,4))
    print("Array \n", a)
    print("\n Sum of Columns use axis =0 \n", a.sum(axis=0))
    print("\n Sum of Rows use axis =1 \n", a.sum(axis=1))
    print("\n Mean of Columns use axis =0 \n", a.mean(axis=0))
    print("\n Mean of Rows use axis =1 \n", a.mean(axis=1))
    print("\n Total mean \n", a.mean())

if __name__ == "__main__":
    test_run()