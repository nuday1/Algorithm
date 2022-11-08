import sys
input = sys.stdin.readline
N,B = map(int,input().split())
H = [list(map(int,input().split())) for _ in range(N)]
Nx = [[0]*N for _ in range(N)]

def multi(U,V):
    n = len(U)
    Z = [[0]*n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i]*V[i][col]
            Z[row][col] = e%1000
    return Z

def square(A,B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A
    else:
        tmp = square(A,B//2)
        if B%2 == 0:
            return multi(tmp,tmp)
        else:
            return multi(multi(tmp,tmp),A)

result = square(H,B)
for r in result:
    print(*r)