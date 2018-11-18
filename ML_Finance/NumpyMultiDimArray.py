# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 07:42:58 2016

@author: DevAdmin
"""
import numpy as np

def test_run():
        print("\n Single Empty Array")
        print(np.empty(5))
        print("\n Double Empty Array")
        print(np.empty((3,2)))
        print("\n 3D Empty Array")
        print(np.empty((5,4,3)))
        
        print("\n 1D  Array with values 1")
        print(np.ones(5))
        print("\n Double  Array with value 1")
        print(np.ones((3,2)))
        print("\n 3D  Array with value 1  ")
        print(np.ones((5,4,3)))
        
        
        print("\n 1D  Array with values 1 as INT")
        print(np.ones(5,dtype=np.int))
        print("\n Double  Array with value 1 as INT")
        print(np.ones((3,2),dtype=np.int))
        print("\n 3D  Array with value 1  as INT")
        print(np.ones((5,4,3),dtype=np.int))


        print("\n 1D  Array with values 0 as INT")
        print(np.zeros(5,dtype=np.int))
        print("\n Double  Array with value 0 as INT")
        print(np.zeros((3,2),dtype=np.int))
        
        
        print("\n Random Value array between 0.0 and 1.0 TUPLE")
        print(np.random.random((3,2)))
        
        print("\n Random Value array between 0.0 and 1.0 NOT A TUPLE")
        print(np.random.rand(3,2))       



        print("\n Gaussian(normal) distribution with mean =0 and SD =1  array value between 0.0 and 1.0 NOT A TUPLE")
        print(np.random.normal(size=(3,2))) 
        

        print("\n Gaussian(normal) distribution with mean =50 and SD =10  array value between 0.0 and 1.0 NOT A TUPLE")
        print(np.random.normal(50,10,size=(3,2)))
        
        
        print("\n Single Int in (0, 10] ")
        print(np.random.randint(10))
        print("\n Single Int in (low, high] ")
        print(np.random.randint(7,10))
        print("\n 5 Rand Int as 1D array ")
        print(np.random.randint(0,10, size=5))
        print("\n 2 X3 array of integer ")
        print(np.random.randint(0,10, size=(2,3)))
        


        
if __name__ == "__main__":
   test_run()
