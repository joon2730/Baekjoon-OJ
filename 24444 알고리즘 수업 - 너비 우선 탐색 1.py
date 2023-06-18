import sys
from collections import deque, defaultdict

def bfs(graph, N, R):  # V : 정점 집합, E : 간선 집합, R : 시작 정점
    visited = [0] * (N + 1)
    Q = deque()
    res = []
    visited[R] = True  # 시작 정점 R을 방문 했다고 표시한다.
    Q.append(R)  # 큐 맨 뒤에 시작 정점 R을 추가한다.
    while Q:
        u = Q.popleft();  # 큐 맨 앞쪽의 요소를 삭제한다.
        res.append(u)
        for v in graph[u]:  # E(u) : 정점 u의 인접 정점 집합.(정점 번호를 오름차순으로 방문한다).
            if visited[v] == False:
                visited[v] = True  # 정점 v를 방문 했다고 표시한다.
                Q.append(v)  # 큐 맨 뒤에 정점 v를 추가한다.
    return res

n, m, R = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(m):
    v, u = map(int, sys.stdin.readline().split())
    graph[v].append(u)
    graph[u].append(v)
for v in graph.values():
    v.sort()
lst = bfs(graph, n, R)
# print(graph)
res = [0] * (n+1)
# print(*lst)
# print(*res)
for i, c in enumerate(lst):
    res[c] = i + 1
for c in res[1:]:
    print(c)

