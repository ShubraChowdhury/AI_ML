# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:02:25 2016

@author: DevAdmin
"""
import numpy as np

def test_run():
    
    a = np.array([(20,30,40,50,10,1),(11,21,31,1,41,51)])
    
    b = a*2
    
    print('\nOriginal: \n',a)
    print('\nMultiply By 2 \n',b)
    
    print('\nElement by Element ADD \n',a+b)
    
    print('\nElement by Element Multiply \n',a*b)
   
    print('\nElement by Element Divide \n',(a / b))
    
if __name__ == "__main__":
    test_run()
