import heapq
import sys
input = sys.stdin.readline

N = int(input())
people_info = []
count = 0

for i in range(N):
    o,h = map(int,input().split())
    people_info.append([o,h])

d = int(input())
people = []

for i in people_info:
    if abs(i[0]-i[1]) <= d:
        people.append(sorted(i))

while len(people)>=count:
    startpoint = 0
    tempcount = 0
    start = heapq.heappop(people)
    startpoint = start[0]
    if start[1] <= startpoint+d:
        tempcount += 1
    temppeople = []
    while people:
        test = heapq.heappop(people)
        if test[0] >= startpoint+d:
            heapq.heappush(people, test)
            break
        elif test[1]<=startpoint+d:
            tempcount += 1
        if test[0] != startpoint:
            heapq.heappush(temppeople, test)
    for i in temppeople:
        heapq.heappush(people,i)
    count = max(count,tempcount)

print(count)