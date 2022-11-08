from itertools import product
list123 = [1, 2, 3]
search = []
count = 0

N = int(input())

for _ in range(N):
    search.append(int(input()))


for C in search:
    for no in range(1,C+1):
        templist=list(product(list123, repeat = no))
        for i in range(len(templist)):
            if sum(templist[i]) == C :
                count += 1
    print(count)
    count = 0