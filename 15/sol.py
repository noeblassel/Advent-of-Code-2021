import numpy as np
filename="input"

grid=np.array([list(map(int,l.strip()))for l in open(filename).readlines()])
risks=np.copy(grid)

h,w=grid.shape

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

