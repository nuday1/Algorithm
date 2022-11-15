import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())

parent = [0]*(N+1)
parent[1] = 1
Nodes = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int,input().split())
    Nodes[a].append(b)
    Nodes[b].append(a)
# print(Nodes)


def set_parent(v):
    for i in Nodes[v]:
        if not parent[i]:
            parent[i] = v
            set_parent(i)

set_parent(1)
[print(i) for i in parent[2::]]