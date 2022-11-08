C = int(input())

for _ in range(C):
    stulist = list(map(int,input().split()))
    aver = sum(stulist[1:])/stulist[0]
    overAver = 0
    for i in stulist[1:]:
        if i > aver :
            overAver += 1
    overAverPer = overAver/stulist[0]*100
    print(f'{overAverPer:.3f}%')