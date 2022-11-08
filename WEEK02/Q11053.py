import sys
input = sys.stdin.readline

A = int(input())
B = list(map(int,sys.stdin.readline().split()))
ans = [0]*A
ans[0] = 1

def count(x):
    if ans[x-1] == 0:
        count(x-1)

    if B[x-1] < B[x]:
        ans[x] = ans[x-1]+1
    else:
        ans[x] = ans[x-1]
    return ans[x]

print(count(A-1))