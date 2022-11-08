import sys
import copy
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
print(arr)

#배열 섞기



#최대값 구하기
arrsum = 0
for i in range(N-1):
    arrsum += abs(arr[i]-arr[i+1])

print(arrsum)