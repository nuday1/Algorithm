A,B,V = map(int,input().split())
curDay = ((V-A)//(A-B))
if V-(curDay*(A-B)) <= A:
    print(curDay+1)
else:
    print(curDay+2)

# if ((V-A)//(A-B))==0 :
#     print(V//(A-B))
# else:
#     print((V//(A-B))+1)