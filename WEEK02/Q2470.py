import sys

N = int(sys.stdin.readline())
Solutions = sorted(map(int,sys.stdin.readline().split()))
result = sys.maxsize
ans = [None]*2
x = 0
y = N-1

while x < y:
    sum = abs(Solutions[x]+Solutions[y])
    if sum < result:
        ans[0] = Solutions[x]; ans[1]=Solutions[y]
        result = sum

    if Solutions[x]+Solutions[y] < 0:
        x += 1

    elif Solutions[x]+Solutions[y] == 0:
        ans[0] = Solutions[x]; ans[1]=Solutions[y]
        break

    else:
        y -= 1

print(ans[0],ans[1])