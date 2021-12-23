height_map=[list(map(int,l.strip())) for l in open("input").readlines()]
h,w=len(height_map),len(height_map[0])
s=0

for j in range(h):
    for i in range(w):
        neighbors=[]
        if j>0:neighbors.append((j-1,i))
        if j<h-1:neighbors.append((j+1,i))
        if i>0:neighbors.append((j,i-1))
        if i<w-1:neighbors.append((j,i+1))

        if all(height_map[j][i]<height_map[y][x] for y,x in neighbors):
            s+=1+height_map[j][i]

print(s)
