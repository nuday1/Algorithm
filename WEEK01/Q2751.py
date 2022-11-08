import sys
N = int(sys.stdin.readline())
x = []
for _ in range(N):
    x.append(int(sys.stdin.readline().strip()))
for _ in sorted(x):
    print(_)