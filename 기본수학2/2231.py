n = int(input())
lst = []
for i in range(1,n+1):
    m = n-i
    l = 0
    for j in str(m):
        l += int(j)
    if m+l == n:
        lst.append(m)
if len(lst) == 0:
    print(0)
else:
    print(min(lst))



# 215
# 예제 입력 1 
# 216
# 예제 출력 1 
# 198