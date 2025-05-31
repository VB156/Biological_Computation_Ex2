import itertools
import numpy as np

def all_possible_subgraphs_edges(num):
    pairs = list(itertools.permutations(range(1, num + 1), 2))
    pairs = [list(c) for c in pairs]
    print(f"n={num}")
    count = 0
    result = []
    for i in range(1, len(pairs) + 1):
        last_one = list(itertools.combinations(pairs, i))
        for c in last_one:
            count += 1
            result.append(np.squeeze(np.array(c)))
    print(f"count={count}")
    for i in range(count):
        print(f"#{i + 1}")
        print(result[i])

all_possible_subgraphs_edges(1)
all_possible_subgraphs_edges(2)
all_possible_subgraphs_edges(3)
all_possible_subgraphs_edges(4)

for i in range(1, 11):
    print(((i*(i-1))/2) ** (i*(i-1)))
