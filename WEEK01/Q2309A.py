l=[]

for i in range(9):
    n = int(input())
    l.append(n)

s = sum(l)
s= s-100            #가짜 둘의 키 합
for i in range(9):
    if (s-l[i]) in l and l[i] != s-l[i]:
        k = l.index(s - l[i])
        l.pop(k)
        l.pop(i)
        break
l.sort()
for i in l:
    print(i)