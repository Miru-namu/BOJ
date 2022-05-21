# 예제 입력 1 
# 2
# 6 12 10
# 30 50 72
# 예제 출력 1 
# 402
# 1203
# 30 50 72
# 6 6 12

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    if h == 1:
        print(100+n)
    elif w == 1:
        print(n*100+1)
    elif n%h == 0:
        print(n*100+(n//h)+1)
    elif n//h == 0:

    else:
        print(n%h*100+(n//h)+1)

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    s = 0
    while n >= h:
        n -= h
        s += 1
    if 
