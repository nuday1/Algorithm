N = int(input())
count = 0


CycleN = N

while True :

    A = CycleN//10
    B = CycleN%10 
    temp = (A+B)%10

    CycleN = B*10+temp

    # print(CycleN)
    count += 1

    if CycleN == N:
        break


print(count)