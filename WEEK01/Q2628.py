w, h = map(int,input().split())
cut = int(input())
cutorder = [None]*cut
for i in range(cut):
    cutorder[i] = list(map(int,input().split()))
cuthor = []
cuthor.append(0)
cutver = []
cutver.append(0)
for i in cutorder:
    if i[0] == 0:
        cuthor.append(i[1])
    else:
        cutver.append(i[1])
cuthor.append(h)
cutver.append(w)
cuthor.sort()
cutver.sort()
area=[]
for i in range(1,len(cuthor)):
    for j in range(1,len(cutver)):
        area.append((cuthor[i]-cuthor[i-1])*(cutver[j]-cutver[j-1]))
print(max(area))