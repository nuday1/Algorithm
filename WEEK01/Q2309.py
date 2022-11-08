import copy
import sys
kids = []

for _ in range(9):
    kids.append(int(sys.stdin.readline()))
sum = [sum(kids)]

def find_kids():
    for i in kids:
        sum2 = copy.deepcopy(sum)
        kids2 = copy.deepcopy(kids)
        if sum[0]-i <= 100:
            continue
        else:
            sum2[0] -= i
            kids2.remove(i)
            for j in kids2:
                if sum2[0]-j == 100:
                    kids2.remove(j)
                    for _ in sorted(kids2):
                        print(_)
                    return
find_kids()