import numpy as np

L=10

grid = np.array([list(map(int, l.strip()))
                 for l in open("input").readlines()])
all_indices={(j,i) for j in range(L) for i in range(L)}
t=0
while 1:
    t+=1
    grid += 1
    still_flashing = True
    flashing_indices = set()

    while still_flashing:
        still_flashing = False
        new_flashing_indices = {(j, i)for j in range(L)for i in range(
            L)if grid[j][i] > 9 and not (j, i) in flashing_indices}
        if new_flashing_indices:
            still_flashing = True
        flashing_indices |= new_flashing_indices
        for j, i in new_flashing_indices:
            if j > 0:
                if i > 0 and not (j-1, i-1) in flashing_indices:
                    grid[j-1, i-1] += 1
                if not (j-1, i) in flashing_indices:
                    grid[j-1, i] += 1
                if i < L-1 and not(j-1, i+1) in flashing_indices:
                    grid[j-1, i+1] += 1
            if j < L-1:
                if i > 0 and not (j+1, i-1) in flashing_indices:
                    grid[j+1, i-1] += 1
                if not (j+1, i) in flashing_indices:
                    grid[j+1, i] += 1
                if i < L-1 and not(j+1, i+1) in flashing_indices:
                    grid[j+1, i+1] += 1
            if i > 0 and not (j, i-1) in flashing_indices:
                grid[j, i-1] += 1
            if i < L-1 and not (j, i+1) in flashing_indices:
                grid[j, i+1] += 1
    for j,i in flashing_indices:
        grid[j,i]=0
    if flashing_indices==all_indices:
        print(t)
        exit()