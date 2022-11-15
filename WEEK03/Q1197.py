import sys
input = sys.stdin.readline

V, E = map(int, input().split())
Vroot = [i for i in range(V+1)]
print(Vroot)
lines = [list(map(int, input().split())) for _ in range(E)]
lines.sort(key=lambda x: x[2])
print(lines)

def find(x):
    print(x,Vroot[x],'현재x와vroot[x]')
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
        print(Vroot[x],'Vroot[x] 내부if')
    print(Vroot[x],'Vroot[x] 외부if')
    return Vroot[x]
result = 0

for s, e, w in lines:
    print(s,e,w,'현재 간선')
    sRoot = find(s)
    eRoot = find(e)
    print(sRoot,eRoot)
    if sRoot != eRoot:
        if sRoot > eRoot:
            Vroot[sRoot] = eRoot
        else:
            Vroot[eRoot] = sRoot
        result += w
    print(result,'현재 result')

print(result)