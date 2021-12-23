import numpy as np
*timers,=map(int,open("input").read().split(","))
Xini=tuple(map(timers.count,range(9)))

A=np.array([[0,1,0,0,0,0,0,0,0],\
            [0,0,1,0,0,0,0,0,0],\
            [0,0,0,1,0,0,0,0,0],\
            [0,0,0,0,1,0,0,0,0],\
            [0,0,0,0,0,1,0,0,0],\
            [0,0,0,0,0,0,1,0,0],\
            [1,0,0,0,0,0,0,1,0],\
            [0,0,0,0,0,0,0,0,1],\
            [1,0,0,0,0,0,0,0,0]\
                ])
n=256#change for part 1 and 2

Apow=np.linalg.matrix_power(A,n)
Xfin=np.dot(Apow,Xini)
print(Xfin.sum())