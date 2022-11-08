N = int(input())
Nlist = []
Hansu = 0

for i in range(1,N+1):
    Nlist.append(str(i))
# print(Nlist)
# print(len(Nlist))

if 1 <= len(Nlist) <=99:
    Hansu += len(Nlist)
else:
    Hansu += 99
# print(Hansu)

for i in Nlist[100::]:
    if int(i[0])-int(i[1]) == int(i[1])-int(i[2]):
        Hansu += 1
print(Hansu)