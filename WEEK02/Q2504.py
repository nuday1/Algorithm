import sys
input = sys.stdin.readline

bracket = list(input().strip())

stack = []
answer = 0
tmp = 1

for i in range(len(bracket)):
    # print(bracket[i],'시작')
    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2
    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3
    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if bracket[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if bracket[i-1] == "[": #스택이랑 비교하는 것이 아닌 브라켓이랑 비교를 해야 곱연산 중복을 막을 수 있다.
            answer += tmp
        stack.pop()
        tmp //= 3
    # print(tmp,answer,stack,'현재 상황')

if stack:
    print(0)
else:
    print(answer)