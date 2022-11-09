import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
sum = 0
for _ in range(N):
    n = int(input())
    heapq.heappush(heap, n)

for _ in range(N-1):
    temp = 0
    temp += heapq.heappop(heap)
    temp += heapq.heappop(heap)
    heapq.heappush(heap, temp)
    sum += temp

print(sum)