import sys

N = int(input())
travel_cost = [list(map(int, input().split())) for _ in range(N)]
min_value = sys.maxsize

def dfs_backtracking(start, next, value, visited):
    global min_value
    
    if len(visited) == N:
        if travel_cost[next][start] != 0:
            min_value = min(min_value, value + travel_cost[next][start])
        return
    for i in range(N):   
        if travel_cost[next][i] != 0 and i not in visited and value < min_value:
            visited.append(i)
            dfs_backtracking(start, i, value+travel_cost[next][i], visited)
            visited.pop()

for i in range(N):
    dfs_backtracking(i, i, 0, [i])

print(min_value)  