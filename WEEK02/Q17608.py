import sys
input = sys.stdin.readline

N = int(input())
height = 0
Stack = [int(input()) for _ in range(N)]
ans = 0

for _ in range(N):
    pop = Stack.pop()
    if pop > height:
        height = pop
        ans += 1

print(ans)