import re

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
num_gens=10

for i in range(num_gens):
    next_seed=""
    for j in range(len(seed)-1):
        if seed[j:j+2] in pair_substitutions:
            next_seed+=seed[j]+pair_substitutions[seed[j:j+2]]
        else:
            next_seed+=seed[j]
    next_seed+=seed[-1]
    seed=next_seed

freq_dict={c:seed.count(c) for c in set(seed)}
freqs=freq_dict.values()
print(max(freqs)-min(freqs))