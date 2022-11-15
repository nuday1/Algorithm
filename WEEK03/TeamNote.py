#입력
import sys
input = sys.stdin.readline

#덱 라이브러리
from collections import deque

#dfs 입력받기
Nodes = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    Nodes[a].append(b)
    Nodes[b].append(a)