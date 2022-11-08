import sys
import itertools

N = int(sys.stdin.readline())
cities = []
for _ in range(N):
    cities.append(list(map(int,sys.stdin.readline().split())))

mincost = sys.maxsize
def min_cost(arraylist):
    global mincost
    def_cost = 0
    for i in range(len(arraylist)-1):
        curcity = cities.index(arraylist[i])
        nextcity = cities.index(arraylist[i+1])
        def_cost += cities[curcity][nextcity]
        if def_cost > mincost:
            return
    mincost = min(mincost,def_cost)

for i in itertools.permutations(cities,N):
    arraylist = list(i)
    arraylist.append(arraylist[0])
    for j in range(len(i)):
        if arraylist[cities.index(arraylist[j])][cities.index(arraylist[j+1])] == 0:
            break
    else:
        min_cost(arraylist)

print(mincost)