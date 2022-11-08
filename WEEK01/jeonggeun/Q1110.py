import sys
N = int(sys.stdin.readline())
ans = 0

def find_cycle(i:int):
    global ans
    ans += 1
    strint = []
    if i < 10 :
        strint.append('0'+str(i))
    else:
        strint.append(str(i))
    for i in range(2):
        strint.append(int(strint[0][i]))
    strint.append(strint[1]+strint[2])
    if strint[3] < 10 :
        strint[3] = '0'+str(strint[3])
    else:
        strint[3] = str(strint[3])
    strint.append(int(strint[0][1]+strint[3][1]))
    if strint[4] == N:
        print(ans)
    else:
        find_cycle(strint[4])

find_cycle(N)