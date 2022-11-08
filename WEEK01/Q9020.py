T = int(input())
nList = []
for _ in range(T):
    nList.append(int(input()))

for i in nList:
    nSosu = []
    sosuList = []
    for s in range(2,i):
        for k in sosuList:
            if s%k==0:
                break
        else:
            sosuList.append(s)
    for j in sosuList:
        if sosuList.count(i-j) != 0 and j <= i/2:
            nSosu.append([j,i-j])
    # print(sosuList)
    # print(nSosu)
    print(nSosu[-1][0],nSosu[-1][1])
