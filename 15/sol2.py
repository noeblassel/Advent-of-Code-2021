import numpy as np
import matplotlib.pyplot as plt
filename="input"

old_grid=np.array([list(map(int,l.strip()))for l in open(filename).readlines()])
h_,w_=old_grid.shape
fac=5

grid=np.zeros(shape=(fac*h_,fac*w_))
for j in range(fac):
    for i in range(fac):
        y,x=j*h_,i*w_
        grid[y:y+h_,x:x+w_]=old_grid+i+j

grid[grid>9]=1+(grid[grid>9]%10)
h,w=grid.shape
risks=np.copy(grid)

for j in range(h):
    for i in range(w):
        if i>0 and j>0:
            risks[h-1-j,w-1-i]+=min(risks[h-j,w-1-i],risks[h-1-j,w-i])
        elif i>0:
            risks[h-1-j,w-1-i]+=risks[h-1-j,w-i]
        elif j>0:
            risks[h-1-j,w-1-i]+=risks[h-j,w-1-i]
risks[0,0]-=grid[0,0]
print(risks[0,0])
plt.imshow(grid)
plt.show()