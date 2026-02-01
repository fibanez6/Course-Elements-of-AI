import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def manhattan_distance(row1, row2):
    return sum(abs(np.asarray(row1) - np.asarray(row2)))


def permutations(data, size):
    for i in range(size):
        for j in range(i + 1, size):
            yield (i, j)

def find_nearest_pair(data):
    N = len(data)

    dist = np.full((N, N), np.inf, dtype=float)

    print(dist)

    for (i, j) in permutations(data, N):
        # print(f"Calculating distance between {i} and {j}")
        distance = manhattan_distance(data[i], data[j])
        dist[i, j] = distance
        dist[j, i] = distance

    print(dist)

    # to get the index of the element with the lowest value 
    index = np.unravel_index(np.argmin(dist), dist.shape)
    print(index)

find_nearest_pair(data)
