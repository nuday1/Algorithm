import sys
sys.setrecursionlimit(10**8)
N = int(sys.stdin.readline())
col = [0]*(N+1)
ans = 0

def promising(i,col):
    k = 1
    flag = True
    while (k < i and flag):
        if col[i] == col[k] or abs(col[i]-col[k]) == (i - k):
            flag = False
        k += 1
    return flag

def n_queens(i,col):
    # print(col)
    global ans
    n = len(col)-1
    if (promising(i,col)):
        if i == n:
            ans += 1
            # print(col[1:n+1])
        else:
            for j in range(1,n+1):
                col[i+1] = j
                n_queens(i+1,col)

n_queens(0,col)
print(ans)