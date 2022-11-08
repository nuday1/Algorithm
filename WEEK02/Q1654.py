import sys

K, N = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline().strip()) for _ in range(K)]

def cut_lines(left, right):
    while left <= right:
        mid = (left+right)//2
        cutted = 0

        for i in lines:
            cutted += i//mid

        if cutted < N:
            right = mid-1
        else:
            left = mid+1
    print(right)

cut_lines(1,max(lines))