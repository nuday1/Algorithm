import itertools

N = int(input())

input_array = list(map(int,input().split()))
result = 0

def result_solve(array):
    global result

    def_result = 0
    for i in range(len(array)-1):
        def_result += abs(array[i]-array[i+1])
    result = max(result,def_result)

for i in itertools.permutations(input_array,N):
    result_solve(i)

print(result)