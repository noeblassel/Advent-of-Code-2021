from collections import deque


def parse_graph(filename):
    G = {}
    for l in open(filename).readlines():
        a, b = l.strip().split("-")
        if not a in G:
            G[a] = []
        if not b in G:
            G[b] = []
        G[a].append(b)
        G[b].append(a)
    return G


def all_paths(filename):
    G = parse_graph(filename)
    paths=[]
    candidates=deque()
    candidates.append(("start",))
    while candidates:
        partial_path=candidates.popleft()
        for d in G[partial_path[-1]]:
            if d!="start":
                if d=="end":
                    paths.append((*partial_path,"end"))
                elif (not(d.islower() and d in partial_path))or(all(partial_path.count(x)<2 for x in partial_path if x.islower())):
                    candidates.append((*partial_path,d))
    return paths

print(len(all_paths("input")))

