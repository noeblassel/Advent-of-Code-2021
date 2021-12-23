import re
import numpy as np

filename="input"
input_file=open(filename).readlines()
pair_substitutions={}

for l in input_file:
    m=re.match("^(..) -> (.)$",l.strip())
    if m:
        a,b=m.groups()
        pair_substitutions[a]=b
    elif l.strip():
        seed=l.strip()

one_grams=''.join(sorted(set("".join(pair_substitutions.keys()))))
d=len(one_grams)

def ngram_to_i(ngram):
    global one_grams,d
    if len(ngram)==2:
        x,y=ngram
        return d*one_grams.find(x)+one_grams.find(y)
    else:
        return d*d+one_grams.find(ngram)

def i_to_ngram(i):
    global one_grams,d
    if i<d*d:
        y=one_grams[i%d]
        x=one_grams[i//d]
        return x+y
    else:
        return one_grams[i%(d*d)]

A=np.zeros(shape=(d*d+d,d*d+d),dtype=np.int)
b=np.zeros(shape=(d*d+d),dtype=np.int)
for x in one_grams:
    for y in one_grams:
        i_x=ngram_to_i(x)
        i_y=ngram_to_i(y)
        i_xy=ngram_to_i(x+y)

        if x+y in pair_substitutions:
            z=pair_substitutions[x+y]
            i_z=ngram_to_i(z)
            i_xz=ngram_to_i(x+z)
            i_zy=ngram_to_i(z+y)
            A[i_x,i_xy]+=1
            A[i_z,i_xy]+=1
            A[i_xz,i_xy]+=1
            A[i_zy,i_xy]+=1
        else:
            A[i_xy,i_xy]+=1
            A[i_x,i_xy]+=1

X=np.zeros(shape=(d*d+d),dtype=np.int)
for x,y in zip(seed,seed[1:]):
    X[ngram_to_i(x+y)]+=1
for x in seed:
    X[ngram_to_i(x)]+=1

b[ngram_to_i(seed[-1])]+=1
X[ngram_to_i(seed[-1])]-=1

n_gens=40
for i in range(n_gens):
    X=np.dot(A,X)+b

freqs=X[-d:]
print(max(freqs)-min(freqs))
print({c:freqs[i] for i,c in enumerate(one_grams)})