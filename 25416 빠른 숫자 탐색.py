from collections import defaultdict

def adjacent_squares(u):
    res = []
    i, j = u
    if i + 1 < R and board[i + 1][j] >= 0:
        res.append((i + 1, j))
    if i - 1 >= 0 and board[i - 1][j] >= 0:
        res.append((i - 1, j))
    if j + 1 < C and board[i][j + 1] >= 0:
        res.append((i, j + 1))
    if j - 1 >= 0 and board[i][j - 1] >= 0:
        res.append((i, j - 1))
    return res

def quick_number_search(u, d):
    global min_depth
    if board[u[0]][u[1]] == 1:
        if d < min_depth or min_depth == -1:
            min_depth = d
        return
    visited[u] = True
    for v in adjacent_squares(u):
        if visited[v] == False:
            quick_number_search(v, d+1)
    visited[u] = False

R = 5
C = 5
board = [[0] * C for _ in range(R)]
for i in range(R):
    l = list(map(int, input().split()))
    for j in range(C):
        board[i][j] = l[j]
cur = tuple(map(int, input().split()))

min_depth = -1
visited = defaultdict(bool)
quick_number_search(cur, 0)
print(min_depth)

