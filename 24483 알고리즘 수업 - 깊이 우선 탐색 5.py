import sys
from collections import defaultdict
sys.setrecursionlimit(10**7)

def dfs(graph, N, R, depth = 0):
    visited[R] = True
    d_lst[R] = depth
    order.append(R)
    for v in graph[R]:
        if visited[v] == False:
            dfs(graph, N, v, depth + 1)
            
n, m, R = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(m):
    v, u = map(int, sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)

for v in graph.values():
    v.sort()
visited = [False] * (n + 1)
order = []
d_lst = [-1] * (n+1)
dfs(graph, n, R)
t_lst = [0] * (n+1)
for i, c in enumerate(order):
    t_lst[c] = i + 1
res = 0
for i in range(1, n+1):
    res += t_lst[i] * d_lst[i]
print(res)

