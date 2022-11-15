import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int,input().split())

visited = [False]*(N+1)

Nodes = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    Nodes[a].append(b)
    Nodes[b].append(a)
# print(Nodes)

count = 0
def dfs(v):
    visited[v] = True
    for i in Nodes[v]:
        if not visited[i]:
            dfs(i)

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)