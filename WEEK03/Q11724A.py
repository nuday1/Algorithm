n, m = map(int, input().split())

parent = [0]*(n+1)
for i in range(1, n+1):
    parent[i] = i

# 최상위 부모를 찾습니다
def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])

# 최상위 부모끼리 비교해서, 더 작은 값으로 바꿉니다. 
def unionParent(parent, x, y):
    x = getParent(parent, x)
    y = getParent(parent, y)

    # 둘중, 더 작은 부모를 갖습니다. 
    if x < y:
        parent[y] = x
    else:
        parent[x] = y
    
for _ in range(m):
    a, b = map(int, input().split())
    unionParent(parent, a, b) # 노드끼리 연결합니다.


result = [] # 최상위 부모노드들만 담을 배열
for a in parent:  # parent의 각 원소마다 최상위 부모노드를 구합니다.
    result.append(getParent(parent, a))
#print(result)

result = result[1:] # 0번째 노드는 필요없으니 잘라줍니다.

print(len(set(result)))