import numpy as np
import re
filename="input"
xlim,ylim=0,0
points=[]
fold_instructions=[]
for l in map(str.strip,open(filename).readlines()):
    if l.startswith("fold"):
        a,b=re.match("^fold along (.)=(\d+)$",l).groups()
        fold_instructions.append((a,int(b)))
    elif l:
        x,y=map(int,l.split(","))
        xlim=max(x,xlim)
        ylim=max(y,ylim)
        points.append((y,x))

xlim+=2 if xlim%2 else 1
ylim+=2 if ylim%2 else 1
paper=np.zeros(shape=(ylim,xlim),dtype=np.int)
print(paper.shape)
virtual_paper=np.zeros_like(paper)
for y,x in points:
    paper[y,x]=1
for t,o in fold_instructions[:1]:
    print(t,o)
    if t=='y':
        ply_a=paper[:o,:]
        ply_b=paper[o+1:,:][::-1,:]
    elif t=='x':
        ply_a=paper[:,:o]
        ply_b=paper[:,o+1:][:,::-1]
    paper=np.bitwise_or(ply_a,ply_b)

print(paper.sum())