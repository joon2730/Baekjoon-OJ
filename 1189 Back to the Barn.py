from collections import deque, defaultdict
import copy

class forest:
    R = int()
    C = int()
    T = list()
    def __init__(self, R, C, T) -> None:
        self.R = R
        self.C = C
        self.T = T
    def adjacent_squares(self, sq):
        res = []
        i, j = sq
        # print(sq)
        if i + 1 < self.R and not self.T[i + 1][j]:
            res.append((i + 1, j))
        if i - 1 >= 0 and not self.T[i - 1][j]:
            res.append((i - 1, j))
        if j + 1 < self.C and not self.T[i][j + 1]:
            res.append((i, j + 1))
        if j - 1 >= 0 and not self.T[i][j - 1]:
            res.append((i, j - 1))
        return res
    def back_to_the_barn_dfs(self, K):
        def dfs(path):
            u = path[-1]
            visited[u] = True
            depth = len(path)
            for v in self.adjacent_squares(u):
                if v == barn:
                    ways.append(path + [v])
                elif not visited[v] and depth + 1 < K:
                    dfs(path + [v])
            visited[u] = False
        visited = defaultdict(bool) 
        bassie = (self.R - 1, 0)
        barn = (0, self.C - 1)
        ways = []
        dfs([bassie])
        return ways

    # returns all paths bassie can take to return to barn with at most K squares
    def back_to_the_barn_bfs(self, K):
        bassie = (self.R - 1, 0)
        barn = (0, self.C - 1)
        ways = []
        Q = deque()
        Q.append([bassie])
        while Q:
            # print('Q:', Q)
            p = Q.popleft()
            # print('p:', p)
            u = p[-1]
            # print('u:', u)
            depth = len(p)
            for v in self.adjacent_squares(u):
                if v == barn:
                    ways.append(p + [v])
                    # print('ways++')
                elif v not in p and depth + 1 < K:
                    # print('Q appended')
                    Q.append(p + [v])
                # else:
                    # print('over k')
            # print('--------')
        return ways

R, C, K = map(int, input().split())
T = [[False] * C for _ in range(R)]

tmp = [['.'] * C for _ in range(R)]
for i in range(R):
    row = input()
    # print(row)
    for j, c in enumerate(row):
        if c == 'T':
            T[i][j] = True
            tmp[i][j] = 'T'
# print(T)

f = forest(R, C, T) 

# both work
# paths_dfs = f.back_to_the_barn_dfs(K)
paths_bfs = f.back_to_the_barn_bfs(K)

paths = list(filter(lambda x: len(x) == K, paths_bfs))
# for p in paths:
#     print()
#     lst = copy.deepcopy(tmp)
#     cnt = 0
#     for cnt, vec in enumerate(p):
#         i, j = vec
#         lst[i][j] = str(cnt)
#     for i in lst:
#         print(''.join(i))
    
print(len(paths))      
                
            


