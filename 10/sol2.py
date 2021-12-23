bracket_dic={">":"<","}":"{",")":"(","]":"["}
score_dic={"<":4,"{":3,"(":1,"[":2}

def is_valid(s):
    from collections import deque
    stack=deque()
    for c in s:
        if c in "<[{(":
            stack.append(c)
        elif c in ">]})":
            o=stack.pop()
            if o!=bracket_dic[c]:
                return False    
    return True

def completion_score(s):
    from collections import deque
    stack=deque()
    for c in s:
        if c in "<[{(":
            stack.append(c)
        elif c in ">]})":
            o=stack.pop()
             
    completion_string="".join(stack)[::-1]
    score=0
    for c in completion_string:
        score=(score*5)+score_dic[c]
    return score
strings=map(str.strip,open("input").readlines())
valid_strings=[s for s in strings if is_valid(s)]

*scores,=map(completion_score,valid_strings)
scores.sort()
print(scores[len(scores)//2])