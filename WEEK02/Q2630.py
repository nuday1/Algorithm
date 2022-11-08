import sys

N = int(sys.stdin.readline())
papers = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

result = []
def cut_papers(x,y,N):
    color = papers[x][y]
    for i in range(x,x+N):
        for j in range(y,y+N):
            if color != papers[i][j]:
                cut_papers(x,y,N//2)
                cut_papers(x+N//2,y,N//2)
                cut_papers(x,y+N//2,N//2)
                cut_papers(x+N//2,y+N//2,N//2)
                return #이게 없으면 왜케 높게 나오지?
    if color == 0:
        result.append(0)
    else:
        result.append(1)


cut_papers(0,0,N)
print(result.count(0))
print(result.count(1))