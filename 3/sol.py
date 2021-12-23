a=[]
for l in open("input").readlines():
    a.append(list(map(int,l.strip())))

*b,=zip(*a)
l=len(b)

gamma=0
epsilon=0
for s in b:
    gamma=(gamma|max(s,key=s.count))<<1
    epsilon=(epsilon|min(s,key=s.count))<<1

print((gamma>>1)*(epsilon>>1))