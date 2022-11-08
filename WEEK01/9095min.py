import sys
input = sys.stdin.readline

n = int(input())
# list = []

def test(num,m):
    global cnt
    if num == m:
        cnt += 1
        # print(list,'p')
        return
    for i in range(1,4):
        if num + i <= m: # 숫자를 + 해도 m를 넘기지 않는다면 진행
            # list.append(i)
            # print(list)
            test(num+i,m)

for _ in range(n):
    cnt = 0
    test_case = int(input())
    for i in range(1,4): # 앞의 자리가 각각 1,2,3에서 나오는 조합을 다 확인
        print(i)
        test(i,test_case)
    # print(cnt)