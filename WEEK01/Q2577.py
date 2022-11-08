A = int(input()) ; B = int(input()) ; C = int(input())
str = str(A * B * C)
num = list(map(int,str))

for i in range(10):
    temp = num.count(i)
    print(temp)