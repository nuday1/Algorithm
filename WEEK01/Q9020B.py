import sys
n = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(n)]
answer=[]
#소수 리스트 만들기
def primeNum(num):
    if num==2 or num==3:
        return num
    else:
        for i in range(2,int(num**(1/2))+1):
            if num%i==0:
                return False
    return num

for i in nums:
    for j in range(i//2,1,-1):
        if primeNum(j) and primeNum(i-j):
            answer.append([j,i-j])
            break               

for i in answer:
    print(str(i[0])+' '+str(i[1]))

#이 답안은 i-j 계산을 통해 j라는 소수를 찾아놓고 이와 대응하는 소수를 찾기에 계산을 덜 한다.