import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

K = int(input())

def dfs(start, group):
    # print(start,group,'현재start,group')
    visited[start] = group

    for i in Nodes[start]:
        if not visited[i]:
            a = dfs(i, -group)
            if not a:
                # print(start,'폴스 리턴')
                return False
        # print(start,i,'현재start,i')
        # print(visited,'현재 visited')
        elif visited[i] == visited[start]:
            # print(start,'연결됨')
            return False
    else:
        return True

for _ in range(K):
    V, E = map(int, input().split())
    Nodes = [[] for _ in range(V+1)]
    visited = [False]*(V + 1)
    for _ in range(E):
        a, b = map(int,input().split())
        Nodes[a].append(b)
        Nodes[b].append(a)
    # print(Nodes)

    for i in range(1, V + 1):
        if not visited[i]:
            result = dfs(i, 1)
            if not result:
                break

    print('YES' if result else 'NO')