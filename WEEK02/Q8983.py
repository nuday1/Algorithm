import sys
input = sys.stdin.readline

M,N,L = map(int,input().split())
X = sorted(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(N)]
A.sort()
ans = 0

def find_M(x,y):
    global ans
    pl = 0
    pr = len(X)-1
    while pl <= pr:
        mid = (pl+pr)//2
        # print(pl,pr,mid)
        # print(X[mid], x-L, x+L)
        # print(abs(X[mid]-x)+y,'사대와 동물 거리')

        if X[mid] < x-L:
            pl = mid+1
            continue
        elif x+L < X[mid]:
            pr = mid-1
            continue
        else:
            if abs(X[mid]-x)+y <=L:
                ans += 1
                break
            else:
                if X[mid] == x:
                    break
                elif X[mid] > x:
                    pr = mid-1
                else:
                    pl = mid+1

for i in A:
    # print(i[0],i[1],'동물 위치 사냥확인')
    find_M(i[0],i[1])

print(ans)