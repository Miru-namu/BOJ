# 수 정렬하기 1

t = int(input())
lst = []
for i in range(t):
    lst.append(int(input()))

lst.sort()

for j in range(len(lst)):
    print(lst[j])

# 예제 입력 1 
# 5
# 5
# 2
# 3
# 4
# 1
# 예제 출력 1 
# 1
# 2
# 3
# 4
# 5
