import sys
input = sys.stdin.readline

t=int(input())
lst = []
for _ in range(t):
    num = int(input())
    if num == 0:
        lst.pop()
    else:
        lst.append(num)
print(sum(lst))





# 예제 입력 1 
# 4
# 3
# 0
# 4
# 0
# 예제 출력 1 
# 0
# 예제 입력 2 
# 10
# 1
# 3
# 5
# 4
# 0
# 0
# 7
# 0
# 0
# 6
# 예제 출력 2 
# 7