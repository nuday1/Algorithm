while True:
    x, y, w, h = input().split()
    x = int(x) ; y = int(y) ; w = int(w); h = int(h)
    if 1 <= w <= 1000 and 1 <= h <= 1000 :
        if 1 <= x <= w-1:
            if 1 <= y <= h-1:
                break

minlength = [x,y,w-x,h-y]
minlength.sort()
print(minlength[0])

# 정답
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))