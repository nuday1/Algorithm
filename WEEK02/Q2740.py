N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M, K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

AxB = [[0]*K for _ in range(N)]
for row in range(N):
    for col in range(K):
        e = 0
        for i in range(M):
            e += A[row][i] * B[i][col]
        AxB[row][col] = e

for r in AxB:
    print(*r)
