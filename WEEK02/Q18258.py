import sys
input = sys.stdin.readline

no = 0
front = 0
rear = 0
queue = []

def __len__() -> int:
    return no

def is_empty() -> bool:
    return no <= 0

def enque(x:int):
    global rear
    global no
    queue.append(x)
    rear += 1
    no += 1

def deque():
    global front
    global no
    x = queue[front]
    front += 1
    no -= 1
    return x

def peek():
    return queue[front]

def back():
    return queue[rear-1]


N = int(input())

for _ in range(N):
    order = input().split()

    if order[0] == 'push':
        enque(order[1])

    elif order[0] == 'pop':
        if is_empty():
            print(-1)
        else:
            print(deque())

    elif order[0] == 'size':
        print(no)

    elif order[0] == 'empty':
        if is_empty():
            print(1)
        else:
            print(0)

    elif order[0] == 'front':
        if is_empty():
            print(-1)
        else:
            print(peek())

    elif order[0] == 'back':
        if is_empty():
            print(-1)
        else:
            print(back())