# lee's algorithm
# see https://en.wikipedia.org/wiki/Lee_algorithm

from collections import deque

def adjacent_squares(u):
    res = []
    i, j = u
    if i + 1 < N and box[i + 1][j] >= 0:
        res.append((i + 1, j))
    if i - 1 >= 0 and box[i - 1][j] >= 0:
        res.append((i - 1, j))
    if j + 1 < M and box[i][j + 1] >= 0:
        res.append((i, j + 1))
    if j - 1 >= 0 and box[i][j - 1] >= 0:
        res.append((i, j - 1))
    return res

def lees_algorithm(lst):
    heuristics = [[-1] * M for _ in range(N)]
    Q = deque()
    for u in lst:
        heuristics[u[0]][u[1]] = 0
        Q.append(u)
    # print(Q)
    while Q:
        u = Q.popleft()
        h = heuristics[u[0]][u[1]]
        for v in adjacent_squares(u):
            if heuristics[v[0]][v[1]] < 0 or heuristics[v[0]][v[1]] > h + 1:
                heuristics[v[0]][v[1]] = h + 1
                Q.append(v)

    # for i in heuristics:
    #     print(i)

    maximum_day = -1
    for i in range(N):
        for j in range(M):
            if heuristics[i][j] == -1 and box[i][j] == 0:
                return -1
            elif heuristics[i][j] > maximum_day:
                maximum_day = heuristics[i][j]
    return maximum_day



M, N = map(int, input().split())
box = [[0] * M for _ in range(N)]
riped = []

for i in range(N):
    l = input().split()
    for j in range(M):
        box[i][j] = int(l[j])
        if int(l[j]) == 1:
            riped.append((i, j))

print(lees_algorithm(riped))

