a, b, c = map(int, input().split())
for i in range(a):
    n = int(input())
    if (c**2+b**2)**(1/2) >= n:
        print("DA")
    else:
        print("NE")



# 예제 입력 1 
# 5 3 4
# 3
# 4
# 5
# 6
# 7
# 예제 출력 1 
# DA
# DA
# DA
# NE
# NE
# 예제 입력 2 
# 2 12 17
# 21
# 20
# 예제 출력 2 
# NE
# DA