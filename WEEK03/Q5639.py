import sys
sys.setrecursionlimit(10 ** 9) # 재귀 허용 깊이를 수동으로 늘려주는 코드


# dfs 탐색
def dfs(start, end):
    # print(start, end, '실행')
    if start > end:
        # print('스타트 초과')
        return
    temp = end+1

    for i in range(start+1, end+1):
        if graph[start] < graph[i]:
            temp = i
            # print(graph[start],graph[i],'오른쪽 생성')
            break
    
    # print(start+1, temp-1, '왼쪽 실행')
    dfs(start+1, temp-1)
    # print(temp, end, '오른쪽 실행')
    dfs(temp, end)
    print(graph[start])


# 입력이 없을때까지 반복하여 입력을 리스트에 추가한다.
graph = []
while True:

    try:
        graph.append(int(sys.stdin.readline()))

    except:
        break

dfs(0, len(graph) - 1)