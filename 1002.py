n=int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x1-x2)**2+(y1-y2)**2)**0.5
    if distance == 0 and r1 == r2:
        print(-1)
    elif r2-r1 > 0:
        if distance+r1 == r2:
            print(1)
    elif r1-r2 > 0:
        if distance+r2 == r1:
            print(1)    
    elif distance == 0 and r1 != r2:
        print(0)
    elif distance == r1+r2:
        print(1)
    elif distance > r1+r2:
        print(0)
    elif distance < r1+r2:
        print(2)



# 예제 입력 1 
# 3
# 0 0 13 40 0 37
# 0 0 3 0 7 4
# 1 1 1 1 1 5
# 예제 출력 1 
# 2
# 1
# 0