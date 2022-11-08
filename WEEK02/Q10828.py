from typing import Any
import sys
input = sys.stdin.readline

N = int(input())

class FixedStack:
    class Empty(Exception):
        pass
    class Full(Exception):
        pass

    def __init__(self, capacity: int=256) ->None:
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0

    def __len__(self) -> int:
        return self.ptr

    def is_empty(self) -> bool:
        return self.ptr <= 0

    def is_full(self) -> bool:
        return self.ptr >= self.capacity

    def push(self, value: Any) -> None:
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr - 1]

    def clear(self) -> None:
        self.ptr = 0

    def find(self, value: Any) -> Any:
        for i in range(self.ptr -1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1

    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0

    def dump(self) -> None:
        if self.is_empty():
            print('스택이 비어 있습니다.')
        else:
            print(self.stk[:self.ptr])

s = FixedStack(100000)

for _ in range(N):
    order = input().split()

    if order[0] == 'push':
        try:
            s.push(order[1])
        except FixedStack.Full:
            print('스택이 가득 차 있습니다.')

    elif order[0] == 'pop':
        try:
            x = s.pop()
            print(x)
        except FixedStack.Empty:
            print(-1)

    elif order[0] == 'size':
        print(len(s))

    elif order[0] == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'top':
        try:
            x = s.peek()
            print(x)
        except FixedStack.Empty:
            print(-1)