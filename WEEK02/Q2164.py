import sys
input = sys.stdin.readline

no = 0
front = 0
rear = 0

def __len__() -> int:
    return no

def is_empty() -> bool:
    return no <= 0

def enque(x:int):
    global rear
    global no
    queue[rear] = x
    if rear == N-1:
        rear = 0
    else:
        rear += 1
    no += 1

def deque():
    global front
    global no
    queue[front] = 0
    if front == N-1:
        front = 0
    else:
        front += 1
    no -= 1

def peek():
    return queue[front]

def back():
    return queue[rear-1]

N = int(input())
queue = [None]*N

for i in range(N):
    enque(i+1)

for _ in range(N-1):
    deque()
    enque(peek())
    deque()

print(sum(queue))