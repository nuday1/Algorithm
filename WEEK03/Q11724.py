import sys
input = sys.stdin.readline

N, M = map(int,input().split())

parent = [0]*(N+1)
for i in range(1,N+1):
    parent[i] = i
# print(parent)

Nodes = []
for _ in range(M):
    a, b = map(int, input().split())
    Nodes.append((a, b))
    Nodes.append((b, a))
Nodes.sort()

def find_parent(parent, i):
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    return parent[i]

def union(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a


for node in Nodes:
    a , b = node
    if find_parent(parent,a) != find_parent(parent,b):
        union(parent,a,b)

# result = 0
# for i in range(1,len(parent)):
#     if parent.count(i):
#         result += 1
# # print(parent)
# print(result)

print(len(set(parent))-1) 