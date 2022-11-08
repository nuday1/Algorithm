import sys
from itertools import *

N,S = map(int,sys.stdin.readline().split())
Nlist = list(map(int,sys.stdin.readline().split()))

cnt = 0

for i in range(1,N+1):
    for j in combinations (Nlist,i):
        if sum(j) == S:
            cnt += 1

print(cnt)


# sum_posi = 0
# sum_nega = 0

# for _ in Nlist:
#     if _ >= 0:
#         sum_posi += _
#     else:
#         sum_nega += _

# def promising(i):

# def find_sumS(i,Nlist):
#     cursum = i
#     if (promising(i)):
#         if i == S:

