N = int(input())
num = list(map(int,input().split()))
count = 0

for i in num:
    for j in range(2,i):
        if i%j ==0:
            break
    else:
        count += 1

if num.count(1) == 1:
    print(count-1)
else:
    print(count)