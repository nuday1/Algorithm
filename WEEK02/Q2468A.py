import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
water_board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


dx = [-1,0,1,0]
dy = [0,1,0,-1]

def sink_DFS(x,y,h):
    for m in range(4): #좌0 상1 우2 하3
        nx = x + dx[m]
        ny = y + dy[m]

        if (0 <= nx < N) and (0 <= ny < N) and not sink_table[nx][ny] and water_board[nx][ny] > h:
            sink_table[nx][ny] = True #이미 건너갔으면 트루처리(다음 계산때 이 지역은 패스함)
            print(sink_table)
            sink_DFS(nx,ny,h)

ans = 1
for k in range(max(map(max, water_board))):
    print(k)
    sink_table = [[False]*N for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(N):
            if water_board[i][j] > k and not sink_table[i][j]:
                count += 1 #최소 물 높이 이상의 땅은 1세이프 먹고 들어감, 그 다음은 여기서 어디까지 연결되어있는지 찾아야함
                sink_table[i][j] = True
                sink_DFS(i,j,k)
    print(count,'safe')
    ans = max(ans, count)

print(water_board)
print(ans)