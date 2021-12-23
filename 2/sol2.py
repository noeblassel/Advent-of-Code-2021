x,y,aim=0,0,0

dir_dic={"forward":(1,1,0),"down":(0,0,1),"up":(0,0,-1)}
for l in open("input").readlines():
    dir,m=l.split()
    dx,dy,da=dir_dic[dir]
    x+=int(m)*dx
    y+=int(m)*dy*aim
    aim+=int(m)*da

print(x*y)