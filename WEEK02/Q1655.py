import heapq
import sys
input = sys.stdin.readline

N = int(input())
leftheap = []
rightheap = []
for i in range(N):
    n = int(input())
    if len(leftheap) == len(rightheap):
        heapq.heappush(leftheap, -n)
    else:
        heapq.heappush(rightheap, n)

    if rightheap and rightheap[0] < -leftheap[0]:
        leftvalue = heapq.heappop(leftheap)
        rightvalue = heapq.heappop(rightheap)

        heapq.heappush(leftheap, -rightvalue)
        heapq.heappush(rightheap, -leftvalue)

    print(-leftheap[0])