import numpy as np
*X,=map(int,open("input").read().split(","))
m=int(np.median(X))
print(sum(abs(x-m)for x in X))