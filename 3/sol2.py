a=[]
for l in open("input").readlines():
    a.append(list(map(int,l.strip())))

*b,=zip(*a)

candidates_o2=a.copy()
candidates_co2=a.copy()
ix_o2=0
ix_co2=0

while len(candidates_o2)>1:
    mcb=max(b[ix_o2],key=b[ix_o2].count)
    if b[ix_o2].count(0)==b[ix_o2].count(1):mcb=1
    candidates_o2=[candidate for candidate in candidates_o2 if candidate[ix_o2]==mcb]
    *b,=zip(*candidates_o2)
    ix_o2+=1

*b,=zip(*a)

while len(candidates_co2)>1:
    lcb=min(b[ix_co2],key=b[ix_co2].count)
    if b[ix_co2].count(0)==b[ix_co2].count(1):lcb=0
    candidates_co2=[candidate for candidate in candidates_co2 if candidate[ix_co2]==lcb]
    *b,=zip(*candidates_co2)
    ix_co2+=1

o2=0
co2=0
for x in candidates_o2[0]:o2=(o2|x)<<1
for x in candidates_co2[0]:co2=(co2|x)<<1
print((o2>>1)*(co2>>1))