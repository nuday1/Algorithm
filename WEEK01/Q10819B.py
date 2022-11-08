import sys

sys.setrecursionlimit(100001)
N = int(input())

input_array = list(map(int,input().split()))
result = 0
input_array.sort()
result_array = sorted(input_array,reverse=True)

def result_solve(array):
    global result

    def_result = 0
    for i in range(len(array)-1):
        def_result += abs(array[i]-array[i+1])
    result = max(result, def_result)

def all_permutations_solve(def_array):
    global result

    result_solve(def_array)

    if def_array == result_array:
        print(result)
        exit()

    for i in range(N-1, 0, -1):
        if def_array[i-1] < def_array[i]:
            for j in range(N-1,0,-1):
                if def_array[i-1] < def_array[j]:
                    def_array[i-1],def_array[j] = def_array[j], def_array[i-1]
                    def_array = def_array[:i] + sorted(def_array[i:])
                    all_permutations_solve(def_array)

all_permutations_solve(input_array)