import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

Nodes = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    Nodes[a].append(b)
    Nodes[b].append(a)
# print(Nodes)

virused = [False]*(N+1)

def dfs(v):
    virused[v] = True
    for i in Nodes[v]:
        if not virused[i]:
            dfs(i)

dfs(1)
print(virused.count(True)-1)