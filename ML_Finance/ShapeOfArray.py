# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 08:12:29 2016

@author: DevAdmin
"""

import numpy as np

def test_run():
    a = np.random.random((5,3))
    print(a)
    print(a.shape)
    
    print("\n Number of Rows \n " , a.shape[0])
    print("\n Number of Columns \n " , a.shape[1])
    
    print("\n Dimension of the Array \n",len(a.shape))
    print("\n Size or number of elements of the Array \n",a.size)
if __name__ == "__main__":
    test_run()
