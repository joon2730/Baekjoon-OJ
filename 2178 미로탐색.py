# lee's algorithm
# see https://en.wikipedia.org/wiki/Lee_algorithm

from collections import deque, defaultdict
import sys

def adjacent_squares(u):
    res = []
    i, j = u
    if i + 1 < N and maze[i + 1][j]:
        res.append((i + 1, j))
    if i - 1 >= 0 and maze[i - 1][j]:
        res.append((i - 1, j))
    if j + 1 < M and maze[i][j + 1]:
        res.append((i, j + 1))
    if j - 1 >= 0 and maze[i][j - 1]:
        res.append((i, j - 1))
    return res

def lees_algorithm(start, end):
    heuristics = [[-1] * M for _ in range(N)]
    heuristics[start[0]][start[1]] = 1
    Q = deque()
    Q.append(start)
    while Q:
        # print(Q)
        u = Q.popleft()
        h = heuristics[u[0]][u[1]]
        for v in adjacent_squares(u):
            if heuristics[v[0]][v[1]] < 0:
                heuristics[v[0]][v[1]] = h + 1
                Q.append(v)
    # print(heuristics)
    # for i in heuristics:
    #     print(i)
    return heuristics[end[0]][end[1]]


N, M = map(int, input().split())
maze = [[0] * M for _ in range(N)]

for i in range(N):
    l = input()
    for j in range(M):
        maze[i][j] = int(l[j])

start = (0, 0)
end = (N-1, M-1)
print(lees_algorithm(start, end))

