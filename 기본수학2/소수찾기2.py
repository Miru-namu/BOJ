a = int(input())
b = int(input())

lst = []
result = []
for i in range(a,b+1):
    lst.append(i)

for j in lst:
    if j == 2:
        result.append(2)
    for k in range(2,j):
        if j%k == 0:
            break
        elif k == j-1:
            result.append(j)

if len(result) > 0:
    print(sum(result))
    print(min(result))
elif len(result) == 0:
    print(-1)






# 예제 입력 1 
# 60
# 100
# 예제 출력 1 
# 620
# 61

# 예제 입력 2 
# 64
# 65
# 예제 출력 2 
# -1