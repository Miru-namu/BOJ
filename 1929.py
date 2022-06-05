a, b = map(int, input().split())
for i in range(a,b+1):
    for j in range(2,i+1):
        if j==i:
            print(i)
        elif i%j == 0:
            break
        


# 3 16
# 예제 출력 1 
# 3
# 5
# 7
# 11
# 13