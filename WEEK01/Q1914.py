import sys
N = int(sys.stdin.readline())
def move(no:int,x:int,y:int):
    if no > 1:
        move(no-1,x,6-x-y)
    print(x,y)
    if no > 1:
        move(no-1,6-x-y,y)

if N > 20:
    print(2**N-1)
else:
    print(2**N-1)
    move(N,1,3)