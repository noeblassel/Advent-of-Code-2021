import numpy as np
from scipy.ndimage.measurements import label

height_map=[list(map(int,l.strip())) for l in open("input").readlines()]
h,w=len(height_map),len(height_map[0])
s=0
height_map=np.array(height_map)
height_map=(height_map<9).astype(np.int)
identified_basins,n_basins=label(height_map)

basin_sizes=[(identified_basins==i).sum() for i in range(1,n_basins+1)]
*_,x,y,z=sorted(basin_sizes)
print(x*y*z)