x,y=0,0

dir_dic={"forward":(1,0),"down":(0,1),"up":(0,-1)}
for l in open("input").readlines():
    dir,m=l.split()
    dx,dy=dir_dic[dir]
    print(dx,dy)
    x+=int(m)*dx
    y+=int(m)*dy

print(x*y)