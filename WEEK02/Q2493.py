import sys
input = sys.stdin.readline
n = int(input())
tops = list(map(int,input().split()))
answer= [0] * n #모두 0으로 초기화 되어 있으므로 확인하려는 탑 높이가 이전 탑들보다 클경우 0을 그대로 유지(수신할 탑 없음)
stack = []
#가장 먼저 만나는 높이가 같거나 큰 탑에서 수신가능
for i in range(len(tops)):
    # print(i,'탑 검증')
    while stack:
        # print(i,'루프문발동')
        if tops[stack[-1][0]]<tops[i]:
            # print('최근 탑 팝')
            stack.pop()
        else:
            # print(answer[i],stack[-1][0]+1,'답 넣기')
            answer[i] = stack[-1][0]+1
            break
    stack.append((i,tops[i]))
    # print(stack,'현재 스택')
print(*answer)