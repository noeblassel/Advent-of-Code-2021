s=0
lengths={"0":6,"1":2,"2":5,"3":5,"4":4,"5":5,"6":6,"7":3,"8":7,"9":6}
disp={"abcefg":"0","cf":"1","acdeg":"2","acdfg":"3","bcdf":"4","abdfg":"5","abdefg":"6","acf":"7","abcdefg":"8","abcdfg":"9"}
lines=open("input").readlines()

for l in lines:
    patterns,outputs=l.split("|")
    *patterns,=map(set,patterns.split())

    one,four,seven,eight=[next(p for p in patterns if len(p)==l) for l in (2,4,3,7)]
    a=seven-one
    zero_hat,six_hat,nine_hat=[p for p in patterns if len(p)==6]
    dce=(eight-zero_hat)|(eight-six_hat)|(eight-nine_hat)
    e=dce-four
    cd=dce&four
    c=cd&one
    d=cd-one
    bf=four-cd
    f=bf&one
    b=bf-one
    g=eight-(a|b|c|d|e|f)
    
    a,b,c,d,e,f,g=map(set.pop,[a,b,c,d,e,f,g])
    trans_tab=str.maketrans(a+b+c+d+e+f+g,"abcdefg")
    decoded_outputs=["".join(sorted(o.translate(trans_tab))) for o in outputs.split()]
    s+=int("".join(map(disp.get,decoded_outputs)))
    

print(s)