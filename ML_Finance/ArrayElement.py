# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:07:18 2016

@author: DevAdmin
"""

import numpy as np

def test_run():
    np.random.seed(693)
    a = np.random.randint(0,10, size=(5,6))  
    print('\n',a,'\n')
    print("Select intersection of 4th Row and 3rd Column \n",a[3,2])
    print("Select First thru second column for first row  \n",a[0,1:3])
    print("Select first 2 rows and first 2 columns  \n",a[0:2,0:2])
    print("START:END:JUMP BY  \n",a[:,1:3:1])
    
    a[:,3] = [1,2,3,4,5]
    
    print(a)
    

if __name__ == "__main__":
   test_run()