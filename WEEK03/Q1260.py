import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int,input().split())
Nodes = []
Nodes.append([])

for _ in range(M):
    Nodes.append(list(map(int, input().split())))
# print(Nodes)

graph = [[] for _ in range(N+1)]
for i in Nodes[1::]:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for _ in range(N+1):
    graph[_].sort()
# print(graph)

visited = [False]*(N+1)
# print(visited)

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for j in graph[v]:
        if not visited[j]:
            dfs(graph, j, visited)

dfs(graph,V,visited)
print()

visited = [False]*(N+1)

def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        temp = queue.popleft()
        print(temp, end=' ')
        for i in graph[temp]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
            
bfs(graph,V,visited)