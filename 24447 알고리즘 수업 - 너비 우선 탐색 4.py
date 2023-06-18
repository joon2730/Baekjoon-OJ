import sys
from collections import deque, defaultdict

def bfs(graph, N, R):  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited = [False] * (N + 1)
    Q = deque()
    order = []
    d_lst = [-1] * (N + 1)
    visited[R] = True  # 시작 정점 R을 방문 했다고 표시한다.
    depth_Q = deque()
    Q.append(R)  # 큐 맨 뒤에 시작 정점 R을 추가한다.
    depth_Q.append(0)
    while Q:
        u = Q.popleft();  # 큐 맨 앞쪽의 요소를 삭제한다.
        d = depth_Q.popleft()
        d_lst[u] = d
        order.append(u)
        for v in graph[u]:  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다).
            if visited[v] == False:
                visited[v] = True  # 정점 v를 방문 했다고 표시한다.
                Q.append(v)  # 큐 맨 뒤에 정점 v를 추가한다.
                depth_Q.append(d+1)
    t_lst = [0] * (n+1)
    for i, c in enumerate(order):
        t_lst[c] = i + 1
    return t_lst, d_lst

n, m, R = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(m):
    v, u = map(int, sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)
for v in graph.values():
    v.sort()
t_lst, d_lst  = bfs(graph, n, R)
res = 0
for i in range(1, n+1):
    res += t_lst[i] * d_lst[i]
print(res)

