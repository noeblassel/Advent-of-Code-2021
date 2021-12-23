import numpy as np
*X,=map(int,open("input").read().split(","))
m=int(np.mean(X))
M=m+1
s=sum(abs(x-m)*(abs(x-m)+1)//2 for x in X)
S=sum(abs(x-M)*(abs(x-M)+1)//2 for x in X)
print(min(s,S))