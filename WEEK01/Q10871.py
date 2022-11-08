N, X = map(int,input().split())
test = list(map(int,input().split()))
for i in range(N):
    if test[i] < X:
            print(test[i], end=' ')