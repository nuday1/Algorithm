import sys
from collections import deque

N, K = map(int,sys.stdin.readline().split())
queue = deque()
ans = []

for i in range(N):
    queue.append(i + 1)

print('<',end='')
while len(queue) > 1:
    for _ in range(K-1):
        queue.append(queue.popleft())
    print(queue.popleft(),end=', ')
else:
    print(queue.pop(),end='>')