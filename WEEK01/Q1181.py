import sys
N = int(sys.stdin.readline())
x = []
for _ in range(N):
    x.append(sys.stdin.readline().strip())
words = list(set(x))
words_len = []
for _ in words:
    words_len.append([len(_),_])
result = sorted(words_len)
for len,word in result:
    print(word)