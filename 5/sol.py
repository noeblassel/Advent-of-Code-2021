import re
import numpy as np


lines=[]

for l in open("input").readlines():
    t=tuple(map(int,re.match("^(\d+),(\d+) -> (\d+),(\d+)$",l).groups()))
    lines.append(t)


lines.sort()
ortho_lines=[l for l in lines if l[0]==l[2] or l[1]==l[3]]
max_x=max(max(l[0],l[2]) for l in ortho_lines)
max_y=max(max(l[1],l[3]) for l in ortho_lines)

canvas=np.zeros(shape=(max_x+1,max_y+1))
for xa,ya,xb,yb in ortho_lines:
    if xa==xb:
        canvas[xa,min(ya,yb):max(ya,yb)+1]+=1
    else:
        canvas[min(xa,xb):max(xa,xb)+1,ya]+=1
print((canvas>1).sum())