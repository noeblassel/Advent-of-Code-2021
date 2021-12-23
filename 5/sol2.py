import re
import numpy as np


lines=[]

for l in open("input").readlines():
    t=tuple(map(int,re.match("^(\d+),(\d+) -> (\d+),(\d+)$",l).groups()))
    lines.append(t)

max_x=max(max(l[0],l[2]) for l in lines)
max_y=max(max(l[1],l[3]) for l in lines)

canvas=np.zeros(shape=(max_x+1,max_y+1))
for xa,ya,xb,yb in lines:
    if xa==xb:
        canvas[xa,min(ya,yb):max(ya,yb)+1]+=1
    elif ya==yb:
        canvas[min(xa,xb):max(xa,xb)+1,ya]+=1
    else:
        if yb-ya==xb-xa:
            for i in range(abs(xb-xa)+1):
                canvas[min(xa,xb)+i,min(ya,yb)+i]+=1
        else:
            for i in range(abs(xb-xa)+1):
                canvas[min(xa,xb)+i,max(ya,yb)-i]+=1
print((canvas>1).sum())