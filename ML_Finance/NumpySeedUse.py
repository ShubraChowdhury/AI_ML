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
    np.random.seed(42)
    
    a = np.random.randint(0,10, size=(5,4))
    print("Array \n", a)

if __name__ == "__main__":
    test_run()