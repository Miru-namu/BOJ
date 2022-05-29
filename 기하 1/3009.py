ali = []
bli = []
result = []
for i in range(3):
    a, b = map(int, input().split())
    ali.append(a)
    bli.append(b)
ali.sort()
bli.sort()

if ali[0] == ali[1]:
    result.append(ali[2])
    pass
elif ali[1] == ali[2]:
    result.append(ali[0])

if bli[0] == bli[1]:
    result.append(bli[2])
    pass
elif bli[1] == bli[2]:
    result.append(bli[0])

print(*result, sep=' ')



# 예제 입력 1 
# 5 5
# 5 7
# 7 5
# 예제 출력 1 
# 7 7
# 예제 입력 2 
# 30 20
# 10 10
# 10 20
# 예제 출력 2 
# 30 10