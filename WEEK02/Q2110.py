import sys

N, C = map(int, sys.stdin.readline().split())
House = [int(sys.stdin.readline().strip()) for _ in range(N)]
House.sort()
length = 0

def set_modems(left, right):
    while left <= right:
        global length
        temp_length = sys.maxsize
        count = 1
        mid = (left+right)//2
        
        setted = House[0]

        for i in House:
            if i - setted >= mid:
                count += 1
                temp_length = min(temp_length,(i - setted))
                setted = i              

        if count >= C :
            length = max(length, temp_length)
            left = mid+1
        else:
            right = mid-1
    print(length)

set_modems(1,max(House)-min(House))