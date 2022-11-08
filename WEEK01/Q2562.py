test = []
for i in range(9):
    test.append(int(input()))
print(max(test))
print(test.index(max(test))+1)