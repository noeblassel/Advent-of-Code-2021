bracket_dic={">":"<","}":"{",")":"(","]":"["}
score_dic={">":25137,"}":1197,")":3,"]":57}

def score(s):
    from collections import deque
    stack=deque()
    for c in s:
        if c in "<[{(":
            stack.append(c)
        elif c in ">]})":
            o=stack.pop()
            if o!=bracket_dic[c]:
                return score_dic[c]
    
    return 0

s=sum(map(score,map(str.strip,open("input").readlines())))
print(s)