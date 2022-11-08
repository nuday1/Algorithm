import sys
input = sys.stdin.readline

N = int(input())
Stack = []

for _ in range(N):
    order = int(input())
    if order == 0:
        Stack.pop()
    else:
        Stack.append(order)

print(sum(Stack))