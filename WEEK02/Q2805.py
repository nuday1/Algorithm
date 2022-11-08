from typing import Any, Sequence
import sys

N, M = map(int, sys.stdin.readline().split())
Trees = sorted(map(int,sys.stdin.readline().split()))

def cut_trees(start, end):
    while start <= end:
        mid = (start+end)//2
        log = 0

        for i in Trees:
            if i - mid > 0:
                log += (i - mid)

        if log < M:
            end = mid-1
        else:
            start = mid+1
    print(end)

cut_trees(1,max(Trees))