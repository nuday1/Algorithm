N = int(input())

for _ in range(N):
    oxlist = list(input())
    countO = 0
    temp = 0
    for j in oxlist:
        if j == 'O':
            temp += 1
            countO += temp
        else:
            temp = 0
    print(countO)


    # print(len(test[i]))
    # print(test[i][0])