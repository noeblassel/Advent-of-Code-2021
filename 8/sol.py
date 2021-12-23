s=0
lengths={"0":6,"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6}
lines=open("input").readlines()

for l in lines:
    _,outputs=l.split("|")
    digits=outputs.split()
    s+=sum(len(d)==lengths[i] for d in digits for i in "1478")

print(s)