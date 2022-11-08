import sys
N = int(sys.stdin.readline())
Nlist = []
for _ in range(N):
    Nlist.append(int(sys.stdin.readline()))
Nlist.sort()

for i in Nlist:
    print(i)